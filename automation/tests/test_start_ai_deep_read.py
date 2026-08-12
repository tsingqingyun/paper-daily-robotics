from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "start_ai_deep_read.py"
TEMPLATE = Path(__file__).resolve().parents[1] / "90_Templates" / "Paper Deep Read.md"


class StartAiDeepReadTests(unittest.TestCase):
    def test_creates_separate_indexed_note_without_overwriting_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            source_dir = vault / "30_Updates" / "2026-08-12"
            source_dir.mkdir(parents=True)
            (vault / "90_Templates").mkdir()
            (vault / "50_Papers").mkdir()
            (vault / "90_Templates" / "Paper Deep Read.md").write_text(
                TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8"
            )
            (vault / "50_Papers" / "精读论文索引.md").write_text(
                "# 精读论文索引\n\n## 精读队列\n\n## 已完成\n", encoding="utf-8"
            )
            source = source_dir / "Paper.md"
            source_text = """---
type: update-item
format_version: 2
url: "https://example.test/paper"
concepts: ["机器人学习"]
---

# Paper: Reliable Robot Learning

## 关键点

- **问题**：Policies fail out of distribution.
- **创新点 / 方法**：We propose calibrated control.
- **证据**：Results show a 12% gain.
- **局限**：摘要未明确说明；需阅读全文核查。
"""
            source.write_text(source_text, encoding="utf-8")
            command = [
                sys.executable,
                str(SCRIPT),
                "--vault",
                str(vault),
                "--note",
                str(source.relative_to(vault)),
                "--level",
                "focused",
            ]
            first = subprocess.run(command, check=True, capture_output=True, text=True)
            self.assertIn("Created deep-read note", first.stdout)
            output = vault / "50_Papers" / "Deep Reads" / "Paper Reliable Robot Learning" / "README.md"
            self.assertTrue(output.is_file())
            manifest = output.with_name("manifest.json")
            self.assertTrue(manifest.is_file())
            self.assertIn('"reading_status": "queued"', manifest.read_text(encoding="utf-8"))
            deep_text = output.read_text(encoding="utf-8")
            self.assertIn("reading_level: L1-focused", deep_text)
            self.assertIn("Results show a 12% gain.", deep_text)
            self.assertIn("## 主张—证据账本", deep_text)
            self.assertEqual(source.read_text(encoding="utf-8"), source_text)
            index = (vault / "50_Papers" / "精读论文索引.md").read_text(encoding="utf-8")
            self.assertIn("Paper: Reliable Robot Learning", index)

            second = subprocess.run(command, check=True, capture_output=True, text=True)
            self.assertIn("Existing deep-read note", second.stdout)
            self.assertEqual(index, (vault / "50_Papers" / "精读论文索引.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
