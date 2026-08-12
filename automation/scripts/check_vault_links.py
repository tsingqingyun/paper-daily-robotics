#!/usr/bin/env python3
"""Check Obsidian wiki links in this vault.

The script is intentionally small and standard-library only.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")


def is_vault_content(path: Path, vault: Path) -> bool:
    relative = path.relative_to(vault)
    if any(part.startswith(".") for part in relative.parts):
        return False
    current = vault
    for part in relative.parts[:-1]:
        current /= part
        if (current / ".git").is_dir():
            return False
    return True


def note_key(path: Path, vault: Path) -> str:
    rel = path.relative_to(vault).with_suffix("")
    return rel.as_posix()


def normalize_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target.removesuffix(".md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault path")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    notes = sorted(path for path in vault.glob("**/*.md") if is_vault_content(path, vault))
    files = [
        path
        for path in vault.glob("**/*")
        if path.is_file() and is_vault_content(path, vault)
    ]
    keys = {note_key(path, vault) for path in notes}
    keys.update(path.relative_to(vault).as_posix() for path in files)
    stems = {}
    for path in notes:
        stems.setdefault(path.stem, []).append(note_key(path, vault))
    for path in files:
        stems.setdefault(path.name, []).append(path.relative_to(vault).as_posix())

    missing = []
    ambiguous = []
    total_links = 0

    for path in notes:
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            total_links += 1
            target = normalize_target(match.group(1))
            if not target:
                continue
            if target in keys:
                continue
            if "/" not in target and target in stems:
                if len(stems[target]) > 1:
                    ambiguous.append((path, target, stems[target]))
                continue
            missing.append((path, target))

    print(f"Notes: {len(notes)}")
    print(f"Wiki links: {total_links}")
    print(f"Missing links: {len(missing)}")
    print(f"Ambiguous stem links: {len(ambiguous)}")

    if missing:
        print("\nMissing:")
        for path, target in missing[:100]:
            print(f"- {path.relative_to(vault)} -> [[{target}]]")
        if len(missing) > 100:
            print(f"... and {len(missing) - 100} more")

    if ambiguous:
        print("\nAmbiguous:")
        for path, target, matches in ambiguous[:50]:
            print(f"- {path.relative_to(vault)} -> [[{target}]] matches {matches}")

    return 1 if missing or ambiguous else 0


if __name__ == "__main__":
    raise SystemExit(main())
