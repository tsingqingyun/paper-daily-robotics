"""Refresh an existing daily reading without refetching/reranking or changing seen state.

All explanations must succeed before notes are rewritten; originals are backed up locally.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
from pathlib import Path

import migrate_ai_notes_compact as migration
import update_info_flow as flow


def refresh(vault: Path, date: str, timeout: int = 900) -> dict:
    digest = vault / "30_Updates" / f"{date} AI Embodied Intelligence Update.md"
    original = digest.read_text()
    references = migration.digest_references(vault, original, date)
    if not references:
        raise ValueError("No referenced papers to refresh")
    items = [migration.parse_detail(path, date, link, title) for link, title, path in references]
    for item in items:
        item["id"] = flow.item_id(item)
    briefing = flow.explain_reading_set(items, vault=vault, run_date=date,
                                      codex_bin="/opt/homebrew/bin/codex", timeout=timeout)
    metadata = migration.historical_run_metadata(original, items)
    backup = vault / "state" / "clarity-backups" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    for path in [digest] + [path for _, _, path in references]:
        dest = (backup / path.relative_to(vault)).with_suffix(".md.backup")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    for item, (_, _, path) in zip(items, references):
        flow.atomic_write_text(path, flow.note_body(item, item["concepts"], item["score"], date))
    flow.atomic_write_text(digest, flow.digest_body(date, items, metadata["candidate_count"], metadata["failures"],
                           metadata["concept_summary"], metadata["repeated_count"], metadata["failure_count"], briefing=briefing))
    result = {"date": date, "papers": len(items), "body_excerpt_papers": sum(bool(i.get("source_context")) for i in items),
              "context_failures": [{"title": i["title"], "error": i["source_context_error"]} for i in items if i.get("source_context_error")],
              "backup": str(backup)}
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    print(json.dumps(refresh(Path(args.vault).resolve(), args.date, args.timeout), ensure_ascii=False, indent=2))
