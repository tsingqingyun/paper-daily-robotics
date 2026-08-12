#!/usr/bin/env python3
"""Create an on-demand deep-reading note from an AI daily paper card.

The command never deletes, moves, or overwrites notes. Existing deep-reading cards
are returned unchanged.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

import update_info_flow as flow


TEMPLATE = Path("90_Templates/Paper Deep Read.md")
INDEX = Path("50_Papers/精读论文索引.md")
DEEP_READ_ROOT = Path("50_Papers/Deep Reads")


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
            metadata[key.strip()] = json.loads(raw)
        except json.JSONDecodeError:
            metadata[key.strip()] = raw
    return metadata, text[end + 5 :]


def key_point(body: str, label: str) -> str:
    match = re.search(rf"(?m)^- \*\*{re.escape(label)}\*\*：\s*(.*?)\s*$", body)
    return match.group(1).strip() if match else "待从全文核验。"


def resolve_source(vault: Path, note: str) -> Path:
    source = Path(note).expanduser()
    if not source.is_absolute():
        source = vault / source
    if source.suffix != ".md":
        source = source.with_suffix(".md")
    source = source.resolve()
    try:
        source.relative_to(vault)
    except ValueError as exc:
        raise ValueError(f"Source note is outside the vault: {source}") from exc
    if not source.is_file():
        raise FileNotFoundError(f"Source note does not exist: {source}")
    return source


def render_template(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    unresolved = sorted(set(re.findall(r"\{\{([^{}]+)\}\}", template)))
    if unresolved:
        raise ValueError(f"Unresolved template fields: {unresolved}")
    return template


def register(index_path: Path, deep_note: Path, source: Path, vault: Path, title: str, level: str) -> None:
    index_text = index_path.read_text(encoding="utf-8")
    deep_link = deep_note.relative_to(vault).with_suffix("").as_posix()
    source_link = source.relative_to(vault).with_suffix("").as_posix()
    entry = f"- [ ] [[{deep_link}|{title}]] · [[{source_link}|摘要快读]] · {level}"
    if f"[[{deep_link}|" in index_text:
        return
    marker = "## 精读队列\n"
    if marker not in index_text:
        raise ValueError(f"Deep-read queue heading is missing: {index_path}")
    updated = index_text.replace(marker, f"{marker}\n{entry}\n", 1)
    flow.atomic_write_text(index_path, updated)


def paper_identifiers(url: str) -> tuple[str, str]:
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url, re.IGNORECASE)
    if not match:
        return "", url
    arxiv_id = match.group(1).removesuffix(".pdf")
    return arxiv_id, f"https://arxiv.org/pdf/{arxiv_id}"


def write_manifest(
    path: Path,
    *,
    title: str,
    level: str,
    url: str,
    source_link: str,
) -> None:
    if path.is_file():
        return
    arxiv_id, pdf_url = paper_identifiers(url)
    manifest = {
        "arxiv_id": arxiv_id,
        "title": title,
        "reading_level": level,
        "reading_status": "queued",
        "created": dt.date.today().isoformat(),
        "report": "README.md",
        "source_url": url,
        "pdf_url": pdf_url,
        "publish_source_pdf": False,
        "source_note": f"{source_link}.md",
    }
    flow.atomic_write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def create_deep_read(vault: Path, note: str, level: str) -> tuple[Path, bool]:
    source = resolve_source(vault, note)
    metadata, body = parse_frontmatter(source.read_text(encoding="utf-8"))
    if metadata.get("type") != "update-item" or metadata.get("format_version") != 2:
        raise ValueError(f"Source is not a format v2 AI paper card: {source}")
    title_match = re.search(r"(?m)^# (.+?)\s*$", body)
    if not title_match:
        raise ValueError(f"Cannot find paper title in {source}")
    title = title_match.group(1).strip()
    source_link = source.relative_to(vault).with_suffix("").as_posix()
    existing_link = str(metadata.get("deep_read_note", "")).strip()
    if existing_link:
        registered = vault / existing_link
        if registered.suffix != ".md":
            registered = registered.with_suffix(".md")
        registered = registered.resolve()
        try:
            registered.relative_to(vault)
        except ValueError as exc:
            raise ValueError(f"Registered deep-read note is outside the vault: {registered}") from exc
        if not registered.is_file():
            raise FileNotFoundError(f"Registered deep-read note does not exist: {registered}")
        register(
            vault / INDEX,
            registered,
            source,
            vault,
            title,
            "L1-focused" if level == "focused" else "L2-full",
        )
        return registered, False
    url = str(metadata.get("url", ""))
    arxiv_id, _ = paper_identifiers(url)
    directory_name = flow.slugify(f"{title} {arxiv_id}" if arxiv_id else title, 120)
    output_dir = vault / DEEP_READ_ROOT / directory_name
    output = output_dir / "README.md"
    manifest_path = output_dir / "manifest.json"
    index_path = vault / INDEX
    reading_level = "L1-focused" if level == "focused" else "L2-full"
    if output.is_file():
        write_manifest(
            manifest_path,
            title=title,
            level=reading_level,
            url=url,
            source_link=source_link,
        )
        register(index_path, output, source, vault, title, reading_level)
        return output, False

    concepts = metadata.get("concepts") if isinstance(metadata.get("concepts"), list) else []
    reading_budget = "10–15 分钟" if level == "focused" else "45–90 分钟"
    template_path = vault / TEMPLATE
    template = template_path.read_text(encoding="utf-8")
    values = {
        "reading_level": reading_level,
        "reading_budget": reading_budget,
        "created": dt.date.today().isoformat(),
        "source_note": source_link,
        "source_note_link": f"[[{source_link}]]",
        "source_note_yaml": flow.yaml_string(source_link),
        "url": url,
        "url_yaml": flow.yaml_string(url),
        "title": title,
        "title_yaml": flow.yaml_string(title),
        "problem": key_point(body, "问题"),
        "method": key_point(body, "创新点 / 方法"),
        "abstract_evidence": key_point(body, "证据"),
        "concepts": " ".join(f"[[{concept}]]" for concept in concepts) or "待连接。",
    }
    rendered = render_template(template, values)
    flow.atomic_write_text(output, rendered)
    write_manifest(
        manifest_path,
        title=title,
        level=reading_level,
        url=url,
        source_link=source_link,
    )
    register(index_path, output, source, vault, title, reading_level)
    return output, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--note", required=True, help="Paper card path, relative to the vault or absolute")
    parser.add_argument("--level", choices=("focused", "full"), default="full")
    args = parser.parse_args()
    vault = Path(args.vault).expanduser().resolve()
    try:
        output, created = create_deep_read(vault, args.note, args.level)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Cannot create deep-read note: {exc}\n")
    action = "Created" if created else "Existing"
    print(f"{action} deep-read note: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
