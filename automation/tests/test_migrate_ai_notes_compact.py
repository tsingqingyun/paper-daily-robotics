from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "migrate_ai_notes_compact.py"


class CompactMigrationTests(unittest.TestCase):
    def test_migrates_only_referenced_ai_notes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            date_dir = vault / "30_Updates" / "2026-08-12"
            date_dir.mkdir(parents=True)
            legacy = """---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv"
url: "https://example.test/paper"
published: "2026-08-11T00:00:00Z"
score: 27
created: 2026-08-12
concepts: ["机器人学习"]
---

# Useful Paper

## 为什么重要

自动筛选分数：27

连接概念：[[机器人学习]]

## 摘要

Robots fail under occlusion. We propose an uncertainty-aware policy. Results show a 12% gain.

## 来源

- Source: arXiv
- URL: https://example.test/paper
- Authors: Ada Robot
- Published: 2026-08-11T00:00:00Z

## 我的判断

- [ ] old placeholder
"""
            referenced = date_dir / "Useful Paper.md"
            referenced.write_text(legacy, encoding="utf-8")
            unrelated = date_dir / "Economics Note.md"
            unrelated.write_text("do not change\n", encoding="utf-8")
            digest = vault / "30_Updates" / "2026-08-12 AI Embodied Intelligence Update.md"
            digest.write_text(
                """---
type: daily-update
created: 2026-08-12
---

# 2026-08-12 AI Embodied Intelligence Update

## 运行摘要

- 候选数量：42
- 其中回填已见条目：0
- 信息源错误：0

## 高价值条目

### [[30_Updates/2026-08-12/Useful Paper|Useful Paper]]
""",
                encoding="utf-8",
            )

            subprocess.run([sys.executable, str(SCRIPT), "--vault", str(vault)], check=True, capture_output=True)
            migrated = referenced.read_text(encoding="utf-8")
            migrated_digest = digest.read_text(encoding="utf-8")
            self.assertIn("format_version: 2", migrated)
            self.assertIn("**证据**：Results show a 12% gain.", migrated)
            self.assertIn("## 必读 1 篇", migrated_digest)
            self.assertIn("- **规模**：42 个候选 → 1 篇入选", migrated_digest)
            self.assertEqual(unrelated.read_text(encoding="utf-8"), "do not change\n")

            before = (migrated, migrated_digest)
            subprocess.run([sys.executable, str(SCRIPT), "--vault", str(vault)], check=True, capture_output=True)
            self.assertEqual(referenced.read_text(encoding="utf-8"), before[0])
            self.assertEqual(digest.read_text(encoding="utf-8"), before[1])


if __name__ == "__main__":
    unittest.main()
