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


if __name__ == "__main__":
    unittest.main()
