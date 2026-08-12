from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "publish_ai_daily.py"
SPEC = importlib.util.spec_from_file_location("publish_ai_daily_test", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PublishAiDailyTests(unittest.TestCase):
    def test_publish_exports_only_digest_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            vault = root / "vault"
            remote = root / "remote.git"
            mirror = root / "mirror"
            run_date = dt.date.today().isoformat()
            detail_dir = vault / "30_Updates" / run_date
            detail_dir.mkdir(parents=True)
            (vault / "state").mkdir(parents=True)
            included = detail_dir / "Included paper.md"
            excluded = detail_dir / "Unselected private note.md"
            included.write_text("# Included\n", encoding="utf-8")
            excluded.write_text("# Must not publish\n", encoding="utf-8")
            digest = vault / "30_Updates" / f"{run_date} AI Embodied Intelligence Update.md"
            digest.write_text(
                f"# Daily\n\n- [[30_Updates/{run_date}/Included paper|Included]]\n- [[世界模型]]\n",
                encoding="utf-8",
            )
            state = {
                "last_run": f"{run_date}T08:10:00",
                "last_output_path": str(digest),
            }
            (vault / "state" / "seen.json").write_text(json.dumps(state), encoding="utf-8")
            for source_relative in MODULE.PUBLIC_AUTOMATION_FILES:
                source = vault / source_relative
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_text(f"fixture for {source_relative}\n", encoding="utf-8")
            private_env = vault / "automations" / "ai" / "env.zsh"
            private_env.write_text("export SECRET=must-not-publish\n", encoding="utf-8")
            deep_read = vault / "50_Papers" / "Deep Reads" / "Test Paper 2608.00001v1"
            deep_read.mkdir(parents=True)
            (vault / "50_Papers" / "Deep Reads" / "README.md").write_text(
                "# Deep Reads\n", encoding="utf-8"
            )
            (deep_read / "README.md").write_text(
                f"---\nreading_status: processed\n---\n\n# Test L2\n\n[[30_Updates/{run_date}/Included paper|Quick note]]\n\n"
                "[[50_Papers/Deep Reads/Test Paper 2608.00001v1/source.pdf|PDF]]\n",
                encoding="utf-8",
            )
            (deep_read / "source.pdf").write_bytes(b"not published")
            (deep_read / "manifest.json").write_text(
                json.dumps(
                    {
                        "title": "Test Paper",
                        "reading_level": "L2-full",
                        "reading_status": "processed",
                        "report": "README.md",
                        "pdf_url": "https://arxiv.org/pdf/2608.00001v1",
                        "source_pdf": "source.pdf",
                        "publish_source_pdf": False,
                    }
                ),
                encoding="utf-8",
            )
            subprocess.run(
                ["git", "init", "--bare", "--initial-branch=main", str(remote)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            args = argparse.Namespace(
                vault=str(vault),
                remote=str(remote),
                repo_dir=str(mirror),
                branch="main",
                date=run_date,
                all=False,
                push_retries=1,
                push_backoff=0,
            )
            commit = MODULE.publish(args)
            self.assertTrue(commit)
            tree = subprocess.run(
                ["git", "--git-dir", str(remote), "ls-tree", "-r", "--name-only", "main"],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout.splitlines()
            self.assertIn(f"daily/{run_date}/index.md", tree)
            self.assertIn(f"daily/{run_date}/items/Included paper.md", tree)
            self.assertNotIn(f"daily/{run_date}/items/Unselected private note.md", tree)
            self.assertIn("automation/scripts/update_info_flow.py", tree)
            self.assertIn("automation/config/sources.json", tree)
            self.assertIn("automation/codex/automation.toml.example", tree)
            self.assertIn("deep-reading/README.md", tree)
            self.assertIn("deep-reading/index-template.md", tree)
            self.assertIn("automation/templates/Paper Deep Read.md", tree)
            self.assertIn("deep-reads/Test Paper 2608.00001v1/README.md", tree)
            self.assertIn("deep-reads/Test Paper 2608.00001v1/manifest.json", tree)
            self.assertNotIn("deep-reads/Test Paper 2608.00001v1/source.pdf", tree)
            self.assertNotIn("automation/env.zsh", tree)
            published_manifest = json.loads(
                subprocess.run(
                    ["git", "--git-dir", str(remote), "show", f"main:daily/{run_date}/manifest.json"],
                    check=True,
                    stdout=subprocess.PIPE,
                    text=True,
                ).stdout
            )
            self.assertEqual(
                published_manifest["source_digest"],
                f"30_Updates/{run_date} AI Embodied Intelligence Update.md",
            )
            published_digest = subprocess.run(
                ["git", "--git-dir", str(remote), "show", f"main:daily/{run_date}/index.md"],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout
            self.assertIn("[Included](items/Included%20paper.md)", published_digest)
            published_deep_read = subprocess.run(
                [
                    "git",
                    "--git-dir",
                    str(remote),
                    "show",
                    "main:deep-reads/Test Paper 2608.00001v1/README.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout
            self.assertIn(f"../../daily/{run_date}/items/Included%20paper.md", published_deep_read)
            self.assertIn("https://arxiv.org/pdf/2608.00001v1", published_deep_read)


if __name__ == "__main__":
    unittest.main()
