# AI & Embodied Intelligence Daily Automation

This directory contains the allowlisted, reusable source for generating and publishing the daily AI / Physical AI / Robotics digest.

## Included

- `scripts/update_info_flow.py`: fetch, rank, deduplicate, and write the digest and detail notes.
- `scripts/migrate_ai_notes_compact.py`: migrate historical AI digests and only their referenced notes to compact format v2 without deleting, moving, or renaming files.
- `scripts/check_vault_links.py`: validate Obsidian Wiki links before publication.
- `scripts/publish_ai_daily.py`: export the verified digest, referenced notes, and this public source allowlist to GitHub.
- `scripts/run_ai_daily.sh`: canonical idempotent entry point with retry, validation, link gate, and publication.
- `config/sources.json`: feed, ranking, and concept classification configuration.
- `tests/`: regression tests for fetch safety, locking, state preservation, link-gate scope, and publication scope.
- `codex/automation.toml.example`: a sanitized Codex scheduled-task example.

Local environment files, state, logs, memories, credentials, backup files, and unrelated vault content are intentionally excluded.

## Run

Requirements: zsh, Git, and Python 3.9 or newer using only the standard library.

1. Place the `scripts`, `tests`, and `config/sources.json` files in an Obsidian vault as shown here; rename `config` to `40_Sources`.
2. Copy `env.example.zsh` to `<vault>/automations/ai/env.zsh` and set the Git remote. Keep this local file private.
3. Run `AI_DAILY_VAULT="/path/to/vault" /bin/zsh scripts/run_ai_daily.sh`.

The wrapper will not publish if generation validation or the vault link gate fails. Publication is limited to the current digest, its explicitly referenced detail notes, and the source allowlist defined in `publish_ai_daily.py`.

## Note format v2

- Daily digest: a 30-second conclusion, 5 must-read papers, 7 scan items, then a compact archive list.
- Paper note: one-line takeaway, problem, method or novelty, abstract-supported evidence, limitation, and research connections.
- Evidence boundary: summaries are extractive from the abstract. Missing evidence or limitations are explicitly marked for full-text review.
- Provenance: the original abstract and source metadata stay available in a folded section.

To migrate existing AI notes, first preview the scope with `python3 scripts/migrate_ai_notes_compact.py --vault "/path/to/vault" --dry-run`, then rerun without `--dry-run`. The migration only rewrites AI digests and their referenced paper notes; it never deletes, moves, or renames files.
