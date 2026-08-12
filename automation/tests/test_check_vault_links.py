from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_vault_links.py"


class CheckVaultLinksTests(unittest.TestCase):
    def test_hidden_publication_mirror_is_excluded(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            (vault / "notes").mkdir()
            (vault / "notes" / "Target.md").write_text("# Target\n", encoding="utf-8")
            (vault / "notes" / "Index.md").write_text("[[Target]]\n", encoding="utf-8")
            mirror = vault / ".github-publish" / "daily"
            mirror.mkdir(parents=True)
            (mirror / "Target.md").write_text("# Mirror\n", encoding="utf-8")

            result = subprocess.run(
                ["python3", str(SCRIPT), "--vault", str(vault)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Notes: 2", result.stdout)
            self.assertIn("Missing links: 0", result.stdout)
            self.assertIn("Ambiguous stem links: 0", result.stdout)

    def test_nested_git_publication_mirror_is_excluded(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            (vault / "notes").mkdir()
            (vault / "notes" / "Target.md").write_text("# Target\n", encoding="utf-8")
            (vault / "notes" / "Index.md").write_text("[[Target]]\n", encoding="utf-8")
            mirror = vault / "automations" / "ai" / "github-daily"
            (mirror / ".git").mkdir(parents=True)
            (mirror / "daily").mkdir()
            (mirror / "daily" / "Target.md").write_text("# Mirror\n", encoding="utf-8")

            result = subprocess.run(
                ["python3", str(SCRIPT), "--vault", str(vault)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Notes: 2", result.stdout)
            self.assertIn("Missing links: 0", result.stdout)
            self.assertIn("Ambiguous stem links: 0", result.stdout)


if __name__ == "__main__":
    unittest.main()
