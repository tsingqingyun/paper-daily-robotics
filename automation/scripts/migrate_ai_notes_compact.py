#!/usr/bin/env python3
"""Migrate AI daily digests and their referenced notes to compact format v2.

Only notes referenced by ``* AI Embodied Intelligence Update.md`` are in scope.
No file is deleted, moved, or renamed.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import update_info_flow as flow


DIGEST_GLOB = "* AI Embodied Intelligence Update.md"
REFERENCE_RE = re.compile(
    r"\[\[(30_Updates/(?P<date>\d{4}-\d{2}-\d{2})/(?P<target>[^|\]\n]+))(?:\|(?P<label>[^\]\n]+))?\]\]"
)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    metadata: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        key, separator, raw = line.partition(":")
        if not separator:
            continue
        raw = raw.strip()
        try:
            value: Any = json.loads(raw)
        except json.JSONDecodeError:
            if raw.lower() in {"true", "false"}:
                value = raw.lower() == "true"
            elif re.fullmatch(r"-?\d+", raw):
                value = int(raw)
            else:
                value = raw
        metadata[key.strip()] = value
    return metadata, text[end + 5 :]


def section(text: str, heading: str, level: int = 2) -> str:
    hashes = "#" * level
    match = re.search(
        rf"(?ms)^{re.escape(hashes)} {re.escape(heading)}\s*\n(.*?)(?=^#{{1,{level}}} |\Z)",
        text,
    )
    return match.group(1).strip() if match else ""


def first_line_value(text: str, label: str) -> str:
    match = re.search(rf"(?m)^- {re.escape(label)}：\s*(.+?)\s*$", text)
    return match.group(1).strip() if match else ""


def parse_authors(text: str) -> list[str]:
    match = re.search(r"(?m)^- Authors:\s*(.*?)\s*$", text)
    if not match or not match.group(1):
        return []
    return [author.strip() for author in match.group(1).split(",") if author.strip()]


def parse_abstract(text: str) -> str:
    compact = re.search(
        r"(?ms)^### 原始摘要\s*\n(.*?)(?=^### 来源\s*$)",
        text,
    )
    if compact:
        return compact.group(1).strip()
    legacy = section(text, "摘要")
    return legacy or "暂无摘要。"


def parse_detail(path: Path, run_date: str, link_path: str, label: str) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(text)
    title_match = re.search(r"(?m)^# (.+?)\s*$", body)
    concepts = metadata.get("concepts")
    if not isinstance(concepts, list):
        concepts = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", section(body, "为什么重要"))
    score = metadata.get("score", 0)
    if not isinstance(score, int):
        try:
            score = int(score)
        except (TypeError, ValueError):
            score = 0
    summary = parse_abstract(body)
    return {
        "title": title_match.group(1).strip() if title_match else label,
        "source": str(metadata.get("source", "")),
        "url": str(metadata.get("url", "")),
        "published": str(metadata.get("published", "")),
        "age_days": metadata.get("age_days", ""),
        "score": score,
        "concepts": [str(concept) for concept in concepts],
        "authors": parse_authors(body),
        "summary": summary,
        "compact_summary": flow.summarize_abstract(summary),
        "link_path": link_path,
        "run_date": run_date,
        "deep_read_status": str(metadata.get("deep_read_status", "")),
        "deep_read_note": str(metadata.get("deep_read_note", "")),
    }


def digest_references(vault: Path, digest_text: str, run_date: str) -> list[tuple[str, str, Path]]:
    references: list[tuple[str, str, Path]] = []
    seen: set[str] = set()
    for match in REFERENCE_RE.finditer(digest_text):
        if match.group("date") != run_date:
            continue
        link_path = match.group(1).removesuffix(".md")
        if link_path in seen:
            continue
        seen.add(link_path)
        label = (match.group("label") or Path(match.group("target")).name).strip()
        source = vault / f"{link_path}.md"
        if not source.is_file():
            raise FileNotFoundError(f"Digest references missing detail note: {source}")
        references.append((link_path, label, source))
    return references


def parse_failures(text: str) -> list[str]:
    match = re.search(
        r"(?ms)^###? 信息源错误\s*\n(.*?)(?=^## |^### |^</details>|\Z)",
        text,
    )
    if not match:
        return []
    return [
        line[2:].strip()
        for line in match.group(1).splitlines()
        if line.startswith("- ") and not line.startswith("- 信息源错误：")
    ]


def historical_run_metadata(text: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    candidate_count: int | str = first_line_value(text, "候选数量") or "历史记录未保存"
    if isinstance(candidate_count, str) and candidate_count.isdigit():
        candidate_count = int(candidate_count)

    repeated_raw = first_line_value(text, "回填已见条目") or first_line_value(text, "其中回填已见条目")
    repeated_count = int(repeated_raw) if repeated_raw.isdigit() else len(re.findall(r"(?m)^- Repeat fallback: yes$", text))

    failures = parse_failures(text)
    failure_raw = first_line_value(text, "信息源错误")
    if failure_raw.isdigit():
        failure_count: int | str = int(failure_raw)
    elif failure_raw:
        failure_count = failure_raw
    else:
        failure_count = len(failures)

    concept_summary = first_line_value(text, "主要技术对象分类")
    if not concept_summary:
        counts = Counter(concept for item in items for concept in item["concepts"])
        concept_summary = "、".join(
            f"{concept} {count}" for concept, count in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
        )
    return {
        "candidate_count": candidate_count,
        "repeated_count": repeated_count,
        "failures": failures,
        "failure_count": failure_count,
        "concept_summary": concept_summary,
    }


def migrate(vault: Path, dry_run: bool = False) -> dict[str, int]:
    digests = sorted((vault / "30_Updates").glob(DIGEST_GLOB))
    detail_paths: set[Path] = set()
    changed_details = 0
    changed_digests = 0

    for digest in digests:
        run_date = digest.name[:10]
        old_digest = digest.read_text(encoding="utf-8")
        items: list[dict[str, Any]] = []
        for link_path, label, detail_path in digest_references(vault, old_digest, run_date):
            detail_paths.add(detail_path)
            item = parse_detail(detail_path, run_date, link_path, label)
            new_detail = flow.note_body(item, item["concepts"], item["score"], run_date)
            old_detail = detail_path.read_text(encoding="utf-8")
            if new_detail != old_detail:
                changed_details += 1
                if not dry_run:
                    flow.atomic_write_text(detail_path, new_detail)
            items.append(item)

        metadata = historical_run_metadata(old_digest, items)
        new_digest = flow.digest_body(
            run_date,
            items,
            metadata["candidate_count"],
            metadata["failures"],
            metadata["concept_summary"],
            metadata["repeated_count"],
            metadata["failure_count"],
        )
        if new_digest != old_digest:
            changed_digests += 1
            if not dry_run:
                flow.atomic_write_text(digest, new_digest)

    return {
        "digests": len(digests),
        "referenced_details": len(detail_paths),
        "changed_digests": changed_digests,
        "changed_details": changed_details,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = migrate(Path(args.vault).expanduser().resolve(), args.dry_run)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
