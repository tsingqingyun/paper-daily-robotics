# AI & Embodied Intelligence Daily Automation

This directory contains the allowlisted, reusable source for generating and publishing the daily AI / Physical AI / Robotics digest.

## Included

- `scripts/update_info_flow.py`: fetch, rank, deduplicate, run one batched semantic explanation, and write the digest and detail notes.
- `scripts/migrate_ai_notes_compact.py`: migrate historical AI digests and only their referenced notes to compact format v2 without deleting, moving, or renaming files.
- `scripts/start_ai_deep_read.py`: create an idempotent, one-paper-per-directory L1/L2 deep-reading card and manifest from a selected daily paper note.
- `scripts/check_vault_links.py`: validate Obsidian Wiki links before publication.
- `scripts/publish_ai_daily.py`: export the verified digest, referenced notes, and this public source allowlist to GitHub.
- `scripts/run_ai_daily.sh`: canonical idempotent entry point with retry, validation, link gate, and publication.
- `config/sources.json`: feed, ranking, and concept classification configuration.
- `tests/`: regression tests for fetch safety, locking, state preservation, link-gate scope, and publication scope.
- `codex/automation.toml.example`: a sanitized Codex scheduled-task example.

Local environment files, state, logs, memories, credentials, backup files, and unrelated vault content are intentionally excluded.

## Run

Requirements: zsh, Git, Python 3.9 or newer using only the standard library, and an authenticated Codex CLI for semantic paper explanations.

1. Place the `scripts`, `tests`, and `config/sources.json` files in an Obsidian vault as shown here; rename `config` to `40_Sources`.
2. Put `templates/Paper Deep Read.md` in `90_Templates`, `deep-reading/README.md` in `10_MOCs` as `AI 论文深读工作流.md`, and `deep-reading/index-template.md` in `50_Papers` as `精读论文索引.md`.
3. Copy `env.example.zsh` to `<vault>/automations/ai/env.zsh` and set the Git remote. Keep this local file private.
4. Run `AI_DAILY_VAULT="/path/to/vault" /bin/zsh scripts/run_ai_daily.sh`.

The wrapper will not publish if generation validation or the vault link gate fails. Publication is limited to the current digest, its explicitly referenced detail notes, completed deep-read reports, and the source allowlist defined in `publish_ai_daily.py`. Source PDFs remain local by default; published reports link to the canonical paper URL.

The arXiv search API remains the primary paper source. If it is rate-limited or unavailable, the updater automatically switches to the configured official arXiv category RSS feeds, records the recovery in the digest and state, and continues ranking the merged paper set. If both the primary endpoint and every fallback for a critical source fail, the run preserves the previous verified state and blocks publication instead of publishing a low-quality news-only digest.

## Note format v3

- Daily digest: an opinionated daily take, trend line, 5 explained must-read papers, 7 scan items, then a compact archive list.
- Paper note: plain-language TL;DR, concrete bottleneck, mechanism, evidence, research relevance, caveat, and verdict.
- Evidence boundary: one Codex call explains all selected abstracts in Chinese, but may not add facts absent from the abstract. Missing evidence is stated explicitly.
- Quality gate: if Codex is unavailable, times out, or returns an incomplete paper set, publication stops and preserves the previous verified state.
- Provenance: the original abstract and source metadata stay available in a folded section.
- Optional precision layer: every paper card points to an L1 focused check or L2 full deep read; deep notes live separately so daily reading stays compact.

The explanation structure adapts the Apache-2.0 `Nech07/dailypaper` review workflow. See `OPEN_SOURCE_NOTICES.md` for attribution.

To migrate existing AI notes, first preview the scope with `python3 scripts/migrate_ai_notes_compact.py --vault "/path/to/vault" --dry-run`, then rerun without `--dry-run`. The migration only rewrites AI digests and their referenced paper notes; it never deletes, moves, or renames files.

To start a deep read, run `python3 scripts/start_ai_deep_read.py --vault "/path/to/vault" --note "30_Updates/YYYY-MM-DD/Paper.md" --level focused` for a 10–15 minute evidence check, or use `--level full` for a 45–90 minute review. The command creates `50_Papers/Deep Reads/<paper>/README.md` plus a publication manifest and does not overwrite the compact paper card. Mark both files `processed` only after the evidence gate is complete.
