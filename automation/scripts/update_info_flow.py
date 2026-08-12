#!/usr/bin/env python3
"""Fetch AI and embodied-intelligence feeds and write Obsidian notes.

The script intentionally uses only Python standard-library modules.
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import fcntl
import hashlib
import html
import http.client
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}

EX_DATAERR = getattr(os, "EX_DATAERR", 65)
EX_UNAVAILABLE = getattr(os, "EX_UNAVAILABLE", 69)
EX_CANTCREAT = getattr(os, "EX_CANTCREAT", 73)
EX_TEMPFAIL = getattr(os, "EX_TEMPFAIL", 75)
EX_CONFIG = getattr(os, "EX_CONFIG", 78)
RETRYABLE_HTTP_STATUS = {408, 425, 429, 500, 502, 503, 504}
FORMAT_VERSION = 2
MUST_READ_COUNT = 5
SCAN_COUNT = 7
UNSTATED_EVIDENCE = "摘要未报告明确实验结论；需阅读全文核查。"
UNSTATED_LIMITATION = "摘要未明确说明；需阅读全文核查。"

PROBLEM_CUES = (
    "however",
    "challenge",
    "bottleneck",
    "struggle",
    "limitation",
    "limited",
    "lack ",
    "fails ",
    "failure",
    "problem",
    "difficult",
    "remain",
)
METHOD_CUES = (
    "we propose",
    "we present",
    "we introduce",
    "we develop",
    "we design",
    "we build",
    "our method",
    "our approach",
    "this work proposes",
    "this paper proposes",
)
EVIDENCE_CUES = (
    "we achieve",
    "achieves",
    "outperform",
    "improves",
    "results show",
    "experiments show",
    "evaluation shows",
    "we show",
    "we demonstrate",
    "success rate",
    "accuracy",
    "precision",
)
LIMITATION_CUES = (
    "limitation",
    "limited to",
    "future work",
    "remains challenging",
    "remain challenging",
    "does not",
    "cannot",
    "only evaluated",
    "only consider",
)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(f".{path.name}.pending")
    with pending.open("w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(pending, path)


def write_json(path: Path, data: Any) -> None:
    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_datetime(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = clean_text(value)
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(value)
        except (TypeError, ValueError, IndexError, OverflowError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def item_age_days(item: dict[str, Any], now: dt.datetime | None = None) -> int | None:
    published_at = parse_datetime(item.get("published", ""))
    if published_at is None:
        return None
    now = now or dt.datetime.now(dt.timezone.utc)
    return max(0, (now - published_at).days)


def recency_bonus(age_days: int | None) -> int:
    if age_days is None:
        return 0
    if age_days <= 3:
        return 8
    if age_days <= 7:
        return 6
    if age_days <= 14:
        return 4
    if age_days <= 30:
        return 2
    return 0


def slugify(value: str, max_len: int = 80) -> str:
    value = clean_text(value)
    value = re.sub(r"[\\/:*?\"<>|#^\[\]]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    if not value:
        value = "untitled"
    return value[:max_len].strip()


def retry_after_seconds(exc: urllib.error.HTTPError, fallback: float) -> float:
    value = exc.headers.get("Retry-After", "") if exc.headers else ""
    if value.isdigit():
        return min(300.0, max(0.0, float(value)))
    if value:
        try:
            retry_at = email.utils.parsedate_to_datetime(value)
            if retry_at.tzinfo is None:
                retry_at = retry_at.replace(tzinfo=dt.timezone.utc)
            return min(300.0, max(0.0, (retry_at - dt.datetime.now(dt.timezone.utc)).total_seconds()))
        except (TypeError, ValueError, OverflowError):
            pass
    return fallback


def fetch(url: str, timeout: int = 25, retries: int = 3, retry_backoff: float = 2.0) -> bytes:
    retries = max(1, retries)
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Obsidian-AI-Embodied-InfoFlow/1.0 (+local research workflow)",
                "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in RETRYABLE_HTTP_STATUS or attempt >= retries:
                raise
            error = exc
            fallback = retry_backoff * (2 ** (attempt - 1))
            delay = retry_after_seconds(exc, fallback)
        except (
            urllib.error.URLError,
            TimeoutError,
            socket.timeout,
            http.client.HTTPException,
            OSError,
        ) as exc:
            if attempt >= retries:
                raise
            error = exc
            delay = retry_backoff * (2 ** (attempt - 1))
        print(
            f"Fetch attempt {attempt}/{retries} failed for {url}; retrying in {delay:.1f}s: {error}",
            file=sys.stderr,
        )
        time.sleep(delay)
    raise RuntimeError(f"unreachable fetch retry state for {url}")


def first_text(node: ET.Element, paths: list[str]) -> str:
    for path in paths:
        found = node.find(path, NS)
        if found is not None and found.text:
            return clean_text(found.text)
    return ""


def first_link_atom(entry: ET.Element) -> str:
    for link in entry.findall("atom:link", NS):
        href = link.attrib.get("href", "")
        rel = link.attrib.get("rel", "alternate")
        if href and rel == "alternate":
            return href
    link = entry.find("atom:link", NS)
    return link.attrib.get("href", "") if link is not None else ""


def parse_feed(raw: bytes, source: dict[str, Any]) -> list[dict[str, Any]]:
    root = ET.fromstring(raw)
    items: list[dict[str, Any]] = []
    source_name = source["name"]

    if root.tag.endswith("feed"):
        for entry in root.findall("atom:entry", NS):
            title = first_text(entry, ["atom:title"])
            link = first_link_atom(entry)
            published = first_text(entry, ["atom:published", "atom:updated"])
            summary = first_text(entry, ["atom:summary", "atom:content"])
            authors = [
                clean_text(author.findtext("atom:name", default="", namespaces=NS))
                for author in entry.findall("atom:author", NS)
            ]
            items.append(
                {
                    "title": title,
                    "url": link,
                    "published": published,
                    "summary": summary,
                    "authors": [a for a in authors if a],
                    "source": source_name,
                    "source_weight": int(source.get("weight", 1)),
                    "source_max_age_days": int(source.get("max_age_days", 0) or 0),
                }
            )
        return items

    channel = root.find("channel")
    rss_items = channel.findall("item") if channel is not None else root.findall(".//item")
    for item in rss_items:
        title = first_text(item, ["title"])
        link = first_text(item, ["link", "guid"])
        published = first_text(item, ["pubDate", "dc:date"])
        summary = first_text(item, ["description", "content:encoded"])
        creator = first_text(item, ["dc:creator", "author"])
        items.append(
            {
                "title": title,
                "url": link,
                "published": published,
                "summary": summary,
                "authors": [creator] if creator else [],
                "source": source_name,
                "source_weight": int(source.get("weight", 1)),
                "source_max_age_days": int(source.get("max_age_days", 0) or 0),
            }
        )
    return items


def item_id(item: dict[str, Any]) -> str:
    key = item.get("url") or f"{item.get('source')}:{item.get('title')}:{item.get('published')}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def score_item(item: dict[str, Any], ranking_terms: dict[str, int]) -> int:
    haystack = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    score = int(item.get("source_weight", 1))
    for term, weight in ranking_terms.items():
        if term.lower() in haystack:
            score += int(weight)
    score += recency_bonus(item_age_days(item))
    return score


def matches_required_terms(item: dict[str, Any], terms: list[str]) -> bool:
    if not terms:
        return True
    haystack = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    return any(term.lower() in haystack for term in terms)


def concept_links(item: dict[str, Any], concept_map: dict[str, list[str]]) -> list[str]:
    haystack = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    links = []
    for note, terms in concept_map.items():
        if any(term.lower() in haystack for term in terms):
            links.append(note)
    return links or ["AI 核心知识地图"]


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def abstract_sentences(value: str) -> list[str]:
    text = clean_text(value)
    if not text:
        return []
    parts = re.split(r"(?<=[.!?。！？])\s+|(?<=[。！？])", text)
    return [part.strip() for part in parts if part.strip()]


def shorten(value: str, limit: int = 280) -> str:
    value = clean_text(value)
    if len(value) <= limit:
        return value
    clipped = value[: limit - 1].rstrip(" ,;:")
    return f"{clipped}…"


def pick_sentence(
    sentences: list[str],
    cues: tuple[str, ...],
    *,
    exclude: set[str] | None = None,
    prefer_numeric: bool = False,
) -> str:
    exclude = exclude or set()
    candidates = [
        sentence
        for sentence in sentences
        if sentence not in exclude and any(cue in sentence.lower() for cue in cues)
    ]
    if prefer_numeric:
        numeric = [sentence for sentence in candidates if re.search(r"\d", sentence)]
        if numeric:
            candidates = numeric
    return candidates[0] if candidates else ""


def summarize_abstract(value: str) -> dict[str, str | bool]:
    sentences = abstract_sentences(value)
    if not sentences:
        return {
            "takeaway": "暂无可用摘要，需打开原文核查。",
            "problem": "摘要未说明。",
            "method": "摘要未说明。",
            "evidence": UNSTATED_EVIDENCE,
            "limitation": UNSTATED_LIMITATION,
            "needs_fulltext": True,
        }

    method = pick_sentence(sentences, METHOD_CUES)
    problem = pick_sentence(sentences, PROBLEM_CUES, exclude={method})
    evidence = pick_sentence(sentences, EVIDENCE_CUES, exclude={method}, prefer_numeric=True)
    limitation = pick_sentence(sentences, LIMITATION_CUES, exclude={method, evidence})

    if not problem:
        problem = sentences[0]
    if not method:
        method = next((sentence for sentence in sentences if sentence != problem), sentences[0])
    if not evidence:
        evidence = UNSTATED_EVIDENCE
    if not limitation:
        limitation = UNSTATED_LIMITATION

    evidence_missing = evidence == UNSTATED_EVIDENCE
    limitation_missing = limitation == UNSTATED_LIMITATION
    takeaway = evidence if not evidence_missing else method
    return {
        "takeaway": shorten(takeaway, 260),
        "problem": shorten(problem, 320),
        "method": shorten(method, 320),
        "evidence": shorten(evidence, 320),
        "limitation": shorten(limitation, 320),
        "needs_fulltext": evidence_missing or limitation_missing,
    }


def note_body(item: dict[str, Any], concepts: list[str], score: int, run_date: str) -> str:
    title = item["title"]
    concept_line = " ".join(f"[[{concept}]]" for concept in concepts)
    authors = ", ".join(item.get("authors") or [])
    summary = (item.get("summary") or "暂无摘要。").strip()
    compact = item.get("compact_summary") or summarize_abstract(summary)
    needs_fulltext = bool(compact["needs_fulltext"])
    return f"""---
type: update-item
tags: [update, ai, embodied-ai]
format_version: {FORMAT_VERSION}
evidence_level: abstract
reading_status: skimmed
needs_fulltext: {str(needs_fulltext).lower()}
summary_method: abstract-extractive
source: {yaml_string(item.get("source", ""))}
url: {yaml_string(item.get("url", ""))}
published: {yaml_string(item.get("published", ""))}
age_days: {item.get("age_days", "")}
score: {score}
created: {run_date}
concepts: [{", ".join(yaml_string(c) for c in concepts)}]
---

# {title}

> [!summary] 一句话结论（基于摘要）
> {compact["takeaway"]}

## 关键点

- **问题**：{compact["problem"]}
- **创新点 / 方法**：{compact["method"]}
- **证据**：{compact["evidence"]}
- **局限**：{compact["limitation"]}

## 研究关联

- **概念**：{concept_line}
- **筛选分数**：{score}
- **阅读状态**：摘要级快读；{('需要全文核查证据或局限' if needs_fulltext else '摘要已提供证据与局限，仍建议按需核对全文')}

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

{summary}

### 来源

- Source: {item.get("source", "")}
- URL: {item.get("url", "")}
{f"- Authors: {authors}" if authors else ""}
- Published: {item.get("published", "")}
- Age days: {item.get("age_days", "unknown")}

</details>
"""


def digest_body(
    run_date: str,
    selected: list[dict[str, Any]],
    candidate_count: int | str,
    failures: list[str],
    concept_summary: str,
    repeated_count: int,
    failure_count: int | str | None = None,
) -> str:
    source_anomalies = len(failures) if failure_count is None else failure_count
    top_item = selected[0] if selected else None
    must_read = selected[:MUST_READ_COUNT]
    scan = selected[MUST_READ_COUNT : MUST_READ_COUNT + SCAN_COUNT]
    archive = selected[MUST_READ_COUNT + SCAN_COUNT :]
    lines = [
        "---",
        "type: daily-update",
        "tags: [update, ai, embodied-ai]",
        f"format_version: {FORMAT_VERSION}",
        "evidence_level: abstract",
        f"created: {run_date}",
        "---",
        "",
        f"# {run_date} AI Embodied Intelligence Update",
        "",
        "> [!summary] 30 秒结论",
        (
            f"> 今日最值得关注：[[{top_item['link_path']}|{top_item['title']}]] — "
            f"{top_item['compact_summary']['takeaway']}"
            if top_item
            else "> 今日没有入选条目。"
        ),
        "",
        f"- **规模**：{candidate_count} 个候选 → {len(selected)} 篇入选；回填 {repeated_count} 篇",
        f"- **主题**：{concept_summary or '无'}",
        f"- **源异常**：{source_anomalies}",
        "",
        f"## 必读 {len(must_read)} 篇",
        "",
    ]
    if not must_read:
        lines.extend(["本次没有入选条目。", ""])
    for index, item in enumerate(must_read, 1):
        compact = item["compact_summary"]
        lines.extend(
            [
                f"### {index}. [[{item['link_path']}|{item['title']}]]",
                "",
                f"- **创新点 / 方法**：{compact['method']}",
                f"- **证据**：{compact['evidence']}",
                "",
            ]
        )

    lines.extend([f"## 扫读 {len(scan)} 篇", ""])
    if not scan:
        lines.extend(["无。", ""])
    else:
        for item in scan:
            lines.append(
                f"- [[{item['link_path']}|{item['title']}]] — {item['compact_summary']['takeaway']}"
            )
        lines.append("")

    lines.extend([f"## 其余存档 {len(archive)} 篇", ""])
    if not archive:
        lines.extend(["无。", ""])
    else:
        for item in archive:
            concepts = " ".join(f"[[{concept}]]" for concept in item.get("concepts", []))
            lines.append(f"- [[{item['link_path']}|{item['title']}]] · {concepts}")
        lines.append("")

    lines.extend(["<details>", "<summary>运行信息与信息源错误</summary>", ""])
    lines.extend(
        [
            f"- 候选数量：{candidate_count}",
            f"- 入选条目：{len(selected)}",
            f"- 回填已见条目：{repeated_count}",
            f"- 最高分论文：{top_item['title'] if top_item else '无'}",
            f"- 最高分论文发布时间：{top_item.get('published', '无') if top_item else '无'}",
            f"- 主要技术对象分类：{concept_summary or '无'}",
            f"- 信息源错误：{source_anomalies}",
        ]
    )
    if failures:
        lines.extend(["", "### 信息源错误", ""])
        lines.extend(f"- {failure}" for failure in failures)
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def write_update_notes(
    vault: Path,
    selected: list[dict[str, Any]],
    config: dict[str, Any],
    candidate_count: int = 0,
    failures: list[str] | None = None,
) -> list[Path]:
    today = dt.date.today().isoformat()
    item_dir = vault / "30_Updates" / today
    item_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    failures = failures or []
    concept_counts: dict[str, int] = {}
    for item in selected:
        for concept in item.get("concepts", []):
            concept_counts[concept] = concept_counts.get(concept, 0) + 1
    repeated_count = sum(1 for item in selected if item.get("repeat_fallback"))
    concept_summary = "、".join(
        f"{concept} {count}" for concept, count in sorted(concept_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    )
    for item in selected:
        score = item["score"]
        concepts = item["concepts"]
        safe_title = slugify(item["title"])
        item["link_path"] = f"30_Updates/{today}/{safe_title}"
        item["compact_summary"] = summarize_abstract(item.get("summary", ""))
        note_name = f"{safe_title}.md"
        note_path = item_dir / note_name
        atomic_write_text(note_path, note_body(item, concepts, score, today))
        written.append(note_path)

    digest_path = vault / "30_Updates" / f"{today} AI Embodied Intelligence Update.md"
    atomic_write_text(
        digest_path,
        digest_body(today, selected, candidate_count, failures, concept_summary, repeated_count),
    )
    written.append(digest_path)
    return written


def update_index(vault: Path) -> None:
    moc = vault / "10_MOCs" / "MOC - 信息流更新.md"
    updates = sorted((vault / "30_Updates").glob("* AI Embodied Intelligence Update.md"), reverse=True)
    lines = [
        "---",
        "type: moc",
        "tags: [moc, update, ai, embodied-ai]",
        f"updated: {dt.date.today().isoformat()}",
        "---",
        "",
        "# MOC - 信息流更新",
        "",
        "## 最近更新",
        "",
    ]
    for path in updates[:30]:
        lines.append(f"- [[{path.stem}]]")
    lines.extend(
        [
            "",
            "## 更新入口",
            "",
            "- [[信息源清单]]",
            "- [[AI 核心知识地图]]",
            "- [[具身智能核心知识地图]]",
            "",
            "## 阅读规则",
            "",
            "- 日报先看“30 秒结论”和“必读”，其余按需扫读。",
            "- 单篇先看“关键点”，需要核据时再展开原始摘要与来源。",
            "- 摘要没有报告证据或局限时，不做推测，标记为“需全文核查”。",
            "",
        ]
    )
    atomic_write_text(moc, "\n".join(lines))


def run(args: argparse.Namespace) -> int:
    vault = Path(args.vault).expanduser().resolve()
    config_path = Path(args.config).expanduser().resolve() if args.config else vault / "40_Sources" / "sources.json"
    config = read_json(config_path, {})
    if not config:
        print(f"Missing config: {config_path}", file=sys.stderr)
        return EX_CONFIG
    feeds = config.get("feeds", [])
    if not feeds:
        print(f"No feeds configured in: {config_path}", file=sys.stderr)
        return EX_CONFIG

    state_path = vault / "state" / "seen.json"
    state = read_json(state_path, {"seen": {}})
    seen: dict[str, Any] = state.setdefault("seen", {})
    failures = []
    candidates: list[dict[str, Any]] = []

    for source in feeds:
        try:
            raw = fetch(
                source["url"],
                timeout=args.timeout,
                retries=args.fetch_retries,
                retry_backoff=args.retry_backoff,
            )
            candidates.extend(parse_feed(raw, source))
            time.sleep(args.sleep)
        except (
            urllib.error.URLError,
            TimeoutError,
            socket.timeout,
            http.client.HTTPException,
            OSError,
            ET.ParseError,
            ValueError,
        ) as exc:
            failures.append(f"{source.get('name')}: {exc} (after {max(1, args.fetch_retries)} attempts)")

    if not candidates:
        print(
            "No feed candidates were fetched; preserving the previous daily note, index, and seen state.",
            file=sys.stderr,
        )
        if failures:
            print("\nFeed failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return EX_TEMPFAIL

    ranking_terms = config.get("ranking_terms", {})
    concept_map = config.get("concept_links", {})
    required_terms = config.get("required_terms_any", [])
    min_score = int(args.min_score or config.get("min_score", 3))
    max_items = int(args.max_items or config.get("max_items_per_run", 20))
    max_age_days = int(args.max_age_days or config.get("max_age_days", 45))
    now_utc = dt.datetime.now(dt.timezone.utc)
    selected = []
    seen_fallback = []
    selected_ids = set()

    for item in candidates:
        if not item.get("title"):
            continue
        if not matches_required_terms(item, required_terms):
            continue
        age_days = item_age_days(item, now_utc)
        source_max_age_days = int(item.get("source_max_age_days") or 0)
        effective_max_age_days = source_max_age_days or max_age_days
        if (
            not args.include_old
            and age_days is not None
            and effective_max_age_days > 0
            and age_days > effective_max_age_days
        ):
            continue
        ident = item_id(item)
        if ident in selected_ids:
            continue
        score = score_item(item, ranking_terms)
        if score < min_score:
            continue
        item["id"] = ident
        item["age_days"] = age_days if age_days is not None else "unknown"
        item["score"] = score
        item["concepts"] = concept_links(item, concept_map)
        if ident in seen and not args.include_seen:
            item["repeat_fallback"] = True
            seen_fallback.append(item)
            selected_ids.add(ident)
            continue
        selected.append(item)
        selected_ids.add(ident)

    def sort_key(item: dict[str, Any]) -> tuple[int, dt.datetime]:
        return (
            item["score"],
            parse_datetime(item.get("published", "")) or dt.datetime.min.replace(tzinfo=dt.timezone.utc),
        )

    selected.sort(
        key=sort_key,
        reverse=True,
    )
    seen_fallback.sort(
        key=sort_key,
        reverse=True,
    )
    if not selected and seen_fallback and not args.include_seen:
        selected = seen_fallback[:max_items]

    selected = selected[:max_items]

    if args.dry_run:
        for item in selected:
            fallback_mark = " repeat" if item.get("repeat_fallback") else ""
            print(f"{item['score']:>3} | {item['source']} | {item['title']}{fallback_mark}")
        if failures:
            print("\nFailures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 0

    try:
        written = write_update_notes(vault, selected, config, candidate_count=len(candidates), failures=failures)
        output_path = str(written[-1]) if written else None
        update_index(vault)
    except OSError as exc:
        print(f"Cannot write daily update: {exc}", file=sys.stderr)
        return EX_CANTCREAT

    now = dt.datetime.now().isoformat(timespec="seconds")
    for item in selected:
        previous = seen.get(item["id"], {})
        seen[item["id"]] = {
            "title": item["title"],
            "url": item.get("url", ""),
            "source": item.get("source", ""),
            "first_seen": previous.get("first_seen", now),
            "last_included": now,
            "score": item["score"],
        }
    state["last_run"] = now
    state["last_output_path"] = output_path
    state["last_failures"] = failures
    state["last_candidate_count"] = len(candidates)
    state["last_selected_count"] = len(selected)
    state["last_repeat_fallback_count"] = sum(1 for item in selected if item.get("repeat_fallback"))
    state["last_top_title"] = selected[0]["title"] if selected else ""
    state["last_top_score"] = selected[0]["score"] if selected else None
    state["last_top_published"] = selected[0].get("published", "") if selected else ""
    state["last_max_age_days"] = max_age_days
    concept_counts: dict[str, int] = {}
    for item in selected:
        for concept in item.get("concepts", []):
            concept_counts[concept] = concept_counts.get(concept, 0) + 1
    state["last_concept_counts"] = dict(sorted(concept_counts.items(), key=lambda kv: (-kv[1], kv[0])))
    try:
        write_json(state_path, state)
    except OSError as exc:
        print(f"Cannot commit seen state: {exc}", file=sys.stderr)
        return EX_CANTCREAT

    print(f"Selected {len(selected)} items from {len(candidates)} candidates.")
    for path in written:
        print(path)
    if failures:
        print("\nFeed failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
    return 0


def acquire_run_lock(vault: Path):
    lock_path = vault / "state" / "ai-daily.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        handle.close()
        return None
    return handle

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Obsidian vault path")
    parser.add_argument("--config", default="", help="Optional sources.json path")
    parser.add_argument("--max-items", type=int, default=0)
    parser.add_argument("--min-score", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=25)
    parser.add_argument("--sleep", type=float, default=0.8, help="Pause between feeds")
    parser.add_argument("--fetch-retries", type=int, default=3, help="Attempts per feed")
    parser.add_argument("--retry-backoff", type=float, default=2.0, help="Base retry backoff in seconds")
    parser.add_argument("--max-age-days", type=int, default=0, help="Skip older parsed items unless --include-old")
    parser.add_argument("--include-seen", action="store_true")
    parser.add_argument("--include-old", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    vault = Path(args.vault).expanduser().resolve()
    try:
        lock_handle = acquire_run_lock(vault)
    except OSError as exc:
        print(f"Cannot create run lock: {exc}", file=sys.stderr)
        return EX_CANTCREAT
    if lock_handle is None:
        print(f"Another AI daily run already holds {vault / 'state' / 'ai-daily.lock'}", file=sys.stderr)
        return EX_UNAVAILABLE
    try:
        return run(args)
    finally:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
        lock_handle.close()


if __name__ == "__main__":
    raise SystemExit(main())
