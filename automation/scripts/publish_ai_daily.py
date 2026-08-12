#!/usr/bin/env python3
"""Publish verified AI daily digests and their referenced notes to a dedicated Git repository."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote


EX_CANTCREAT = getattr(os, "EX_CANTCREAT", 73)
EX_TEMPFAIL = getattr(os, "EX_TEMPFAIL", 75)
EX_CONFIG = getattr(os, "EX_CONFIG", 78)
WIKI_LINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")
DIGEST_SUFFIX = " AI Embodied Intelligence Update.md"
PUBLIC_AUTOMATION_FILES = {
    "scripts/update_info_flow.py": "automation/scripts/update_info_flow.py",
    "scripts/migrate_ai_notes_compact.py": "automation/scripts/migrate_ai_notes_compact.py",
    "scripts/start_ai_deep_read.py": "automation/scripts/start_ai_deep_read.py",
    "scripts/check_vault_links.py": "automation/scripts/check_vault_links.py",
    "scripts/publish_ai_daily.py": "automation/scripts/publish_ai_daily.py",
    "scripts/run_ai_daily.sh": "automation/scripts/run_ai_daily.sh",
    "tests/test_update_info_flow.py": "automation/tests/test_update_info_flow.py",
    "tests/test_migrate_ai_notes_compact.py": "automation/tests/test_migrate_ai_notes_compact.py",
    "tests/test_start_ai_deep_read.py": "automation/tests/test_start_ai_deep_read.py",
    "tests/test_publish_ai_daily.py": "automation/tests/test_publish_ai_daily.py",
    "tests/test_check_vault_links.py": "automation/tests/test_check_vault_links.py",
    "40_Sources/sources.json": "automation/config/sources.json",
    "automations/ai/README.public.md": "automation/README.md",
    "automations/ai/env.example.zsh": "automation/env.example.zsh",
    "automations/ai/automation.example.toml": "automation/codex/automation.toml.example",
    "90_Templates/Paper Deep Read.md": "automation/templates/Paper Deep Read.md",
    "10_MOCs/AI 论文深读工作流.md": "deep-reading/README.md",
    "50_Papers/精读论文索引.md": "deep-reading/index-template.md",
}


class PublishError(RuntimeError):
    def __init__(self, message: str, exit_code: int = EX_TEMPFAIL):
        super().__init__(message)
        self.exit_code = exit_code


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(f".{path.name}.pending")
    with pending.open("w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(pending, path)


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def run_command(
    command: list[str],
    *,
    cwd: Path | None = None,
    check: bool = True,
    timeout: int = 180,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise PublishError(f"{' '.join(command)} failed: {detail}")
    return result


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run_command(["git", "-C", str(repo), *args], check=check)


def normalize_remote(value: str) -> str:
    return value.strip().removesuffix("/").removesuffix(".git")


def ensure_repository(repo: Path, remote: str, branch: str) -> None:
    if (repo / ".git").is_dir():
        configured = git(repo, "remote", "get-url", "origin").stdout.strip()
        if normalize_remote(configured) != normalize_remote(remote):
            raise PublishError(
                f"Publication mirror origin mismatch: configured={configured!r}, requested={remote!r}",
                EX_CONFIG,
            )
    else:
        if repo.exists() and any(repo.iterdir()):
            raise PublishError(f"Publication mirror is not empty and is not a Git repository: {repo}", EX_CONFIG)
        repo.parent.mkdir(parents=True, exist_ok=True)
        run_command(["git", "clone", remote, str(repo)])

    current_branch = git(repo, "branch", "--show-current", check=False).stdout.strip()
    if not current_branch:
        git(repo, "switch", "-c", branch)
    elif current_branch != branch:
        local_branch = git(repo, "show-ref", "--verify", f"refs/heads/{branch}", check=False)
        if local_branch.returncode == 0:
            git(repo, "switch", branch)
        else:
            git(repo, "switch", "-c", branch)

    remote_head = git(repo, "ls-remote", "--heads", "origin", branch)
    if remote_head.stdout.strip():
        git(repo, "pull", "--rebase", "origin", branch)

    if not git(repo, "config", "user.name", check=False).stdout.strip():
        git(repo, "config", "user.name", "AI Daily Automation")
    if not git(repo, "config", "user.email", check=False).stdout.strip():
        git(repo, "config", "user.email", "ai-daily@localhost")


def parse_wiki_target(raw: str) -> tuple[str, str]:
    target, _, alias = raw.partition("|")
    target = target.split("#", 1)[0].strip().removesuffix(".md")
    return target, (alias.strip() or Path(target).name)


def referenced_notes(vault: Path, digest_text: str, run_date: str) -> dict[str, Path]:
    date_root = (vault / "30_Updates" / run_date).resolve()
    references: dict[str, Path] = {}
    for match in WIKI_LINK_RE.finditer(digest_text):
        target, _ = parse_wiki_target(match.group(1))
        vault_target = target.removeprefix("30_Updates/")
        if not vault_target.startswith(f"{run_date}/"):
            continue
        source = (vault / "30_Updates" / f"{vault_target}.md").resolve()
        try:
            source.relative_to(date_root)
        except ValueError as exc:
            raise PublishError(f"Unsafe daily-note link outside {date_root}: {target}", EX_CONFIG) from exc
        if not source.is_file():
            raise PublishError(f"Digest references a missing detail note: {source}", EX_CONFIG)
        references[target] = source
    return references


def github_digest(digest_text: str, run_date: str, references: dict[str, Path]) -> str:
    def replace(match: re.Match[str]) -> str:
        target, label = parse_wiki_target(match.group(1))
        source = references.get(target)
        if source is None:
            return match.group(0)
        return f"[{label}](items/{quote(source.name)})"

    return WIKI_LINK_RE.sub(replace, digest_text)


def verify_current_state(vault: Path, run_date: str, digest: Path) -> None:
    state_path = vault / "state" / "seen.json"
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PublishError(f"Cannot read verified state {state_path}: {exc}", EX_CONFIG) from exc
    if not str(state.get("last_run", "")).startswith(run_date):
        raise PublishError(f"State is stale for {run_date}: last_run={state.get('last_run')!r}", EX_CONFIG)
    output = state.get("last_output_path")
    if not output or Path(output).expanduser().resolve() != digest.resolve():
        raise PublishError(f"State output does not match today's digest: {output!r}", EX_CONFIG)


def export_date(vault: Path, repo: Path, run_date: str, verify_state: bool) -> list[str]:
    digest = vault / "30_Updates" / f"{run_date}{DIGEST_SUFFIX}"
    if not digest.is_file():
        raise PublishError(f"Daily digest does not exist: {digest}", EX_CONFIG)
    if verify_state:
        verify_current_state(vault, run_date, digest)

    digest_text = digest.read_text(encoding="utf-8")
    references = referenced_notes(vault, digest_text, run_date)
    destination = repo / "daily" / run_date
    items_dir = destination / "items"
    items_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_text(destination / "index.md", github_digest(digest_text, run_date, references))
    for source in references.values():
        atomic_write_text(items_dir / source.name, source.read_text(encoding="utf-8"))

    manifest = {
        "date": run_date,
        "source_digest": digest.relative_to(vault).as_posix(),
        "published_items": [source.name for source in references.values()],
        "published_item_count": len(references),
    }
    atomic_write_json(destination / "manifest.json", manifest)
    return [f"daily/{run_date}"]


def export_automation(vault: Path, repo: Path) -> list[str]:
    destinations: set[str] = set()
    for source_relative, destination_relative in PUBLIC_AUTOMATION_FILES.items():
        source = vault / source_relative
        if not source.is_file():
            raise PublishError(f"Public automation source is missing: {source}", EX_CONFIG)
        destination = repo / destination_relative
        atomic_write_text(destination, source.read_text(encoding="utf-8"))
        destinations.add(Path(destination_relative).parts[0])
    return sorted(destinations)


def normalize_existing_manifests(repo: Path) -> list[str]:
    changed: list[str] = []
    for path in sorted((repo / "daily").glob("*/manifest.json")):
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise PublishError(f"Cannot normalize publication manifest {path}: {exc}", EX_CONFIG) from exc
        run_date = str(manifest.get("date") or path.parent.name)
        source_digest = f"30_Updates/{run_date}{DIGEST_SUFFIX}"
        if manifest.get("source_digest") == source_digest:
            continue
        manifest["source_digest"] = source_digest
        atomic_write_json(path, manifest)
        changed.append(path.relative_to(repo).as_posix())
    return changed


def update_readme(repo: Path) -> None:
    dates = sorted(
        (path.parent.name for path in (repo / "daily").glob("*/index.md")),
        reverse=True,
    )
    lines = [
        "# AI & Embodied Intelligence Daily",
        "",
        "Verified daily AI / Physical AI / Robotics digests exported from the local Obsidian workflow.",
        "Each digest, its explicitly referenced detail notes, and the allowlisted automation source are published.",
        "",
        "## Automation",
        "",
        "- [Source code and setup](automation/README.md)",
        "- [Optional L1/L2 deep-reading workflow](deep-reading/README.md)",
        "",
        "## Daily updates",
        "",
    ]
    lines.extend(f"- [{run_date}](daily/{run_date}/index.md)" for run_date in dates)
    lines.append("")
    atomic_write_text(repo / "README.md", "\n".join(lines))


def push_with_retry(repo: Path, branch: str, retries: int, backoff: float) -> None:
    retries = max(1, retries)
    for attempt in range(1, retries + 1):
        result = git(repo, "push", "-u", "origin", f"HEAD:{branch}", check=False)
        if result.returncode == 0:
            return
        detail = (result.stderr or result.stdout).strip()
        if attempt >= retries:
            raise PublishError(f"Git push failed after {retries} attempts: {detail}")
        delay = backoff * (2 ** (attempt - 1))
        print(f"Git push attempt {attempt}/{retries} failed; retrying in {delay:.1f}s: {detail}", file=sys.stderr)
        time.sleep(delay)


def publish(args: argparse.Namespace) -> str:
    vault = Path(args.vault).expanduser().resolve()
    repo = (
        Path(args.repo_dir).expanduser().resolve()
        if args.repo_dir
        else vault / "automations" / "ai" / "github-daily"
    )
    remote = args.remote or os.environ.get("AI_DAILY_GITHUB_REMOTE", "")
    if not remote:
        raise PublishError("AI_DAILY_GITHUB_REMOTE is not configured", EX_CONFIG)

    ensure_repository(repo, remote, args.branch)
    if args.all:
        dates = sorted(path.name[:10] for path in (vault / "30_Updates").glob(f"*{DIGEST_SUFFIX}"))
    else:
        dates = [args.date or dt.date.today().isoformat()]
    if not dates:
        raise PublishError("No AI daily digests were found", EX_CONFIG)

    stage_paths = ["README.md"]
    for run_date in dates:
        stage_paths.extend(export_date(vault, repo, run_date, verify_state=not args.all))
    stage_paths.extend(export_automation(vault, repo))
    stage_paths.extend(normalize_existing_manifests(repo))
    update_readme(repo)
    git(repo, "add", "--", *stage_paths)

    staged = git(repo, "diff", "--cached", "--quiet", check=False)
    if staged.returncode not in (0, 1):
        raise PublishError(f"Cannot inspect staged publication changes: {staged.stderr.strip()}")
    if staged.returncode == 1:
        message = f"publish AI daily {dates[-1]}" if len(dates) == 1 else f"publish AI daily archive through {dates[-1]}"
        git(repo, "commit", "-m", message)
    head = git(repo, "rev-parse", "HEAD").stdout.strip()
    push_with_retry(repo, args.branch, args.push_retries, args.push_backoff)
    return head


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--remote", default="")
    parser.add_argument("--repo-dir", default="")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--date", default="")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument("--push-backoff", type=float, default=10.0)
    args = parser.parse_args()
    if args.all and args.date:
        parser.error("--all and --date are mutually exclusive")

    vault = Path(args.vault).expanduser().resolve()
    status_path = vault / "state" / "ai-daily.publish.json"
    run_date = args.date or dt.date.today().isoformat()
    try:
        commit = publish(args)
    except (PublishError, OSError, subprocess.SubprocessError) as exc:
        exit_code = exc.exit_code if isinstance(exc, PublishError) else EX_CANTCREAT
        try:
            atomic_write_json(
                status_path,
                {
                    "last_publish_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
                    "last_publish_status": "failed",
                    "last_publish_date": run_date,
                    "last_publish_remote": args.remote or os.environ.get("AI_DAILY_GITHUB_REMOTE", ""),
                    "last_publish_error": str(exc),
                },
            )
        except OSError:
            pass
        print(f"Publication failed: {exc}", file=sys.stderr)
        return exit_code

    atomic_write_json(
        status_path,
        {
            "last_publish_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            "last_publish_status": "success",
            "last_publish_date": run_date,
            "last_publish_remote": args.remote or os.environ.get("AI_DAILY_GITHUB_REMOTE", ""),
            "last_publish_commit": commit,
            "last_publish_error": "",
        },
    )
    print(f"Published AI daily update at commit {commit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
