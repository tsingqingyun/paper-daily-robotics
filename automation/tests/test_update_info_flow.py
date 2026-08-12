from __future__ import annotations

import argparse
import fcntl
import importlib.util
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "update_info_flow.py"
SPEC = importlib.util.spec_from_file_location("update_info_flow_test", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self) -> bytes:
        return self.payload


class UpdateInfoFlowTests(unittest.TestCase):
    def test_fetch_retries_transient_network_failure(self):
        side_effects = [urllib.error.URLError("temporary"), FakeResponse(b"ok")]
        with mock.patch.object(MODULE.urllib.request, "urlopen", side_effect=side_effects) as opener:
            with mock.patch.object(MODULE.time, "sleep") as sleep:
                payload = MODULE.fetch("https://example.test/feed", retries=3, retry_backoff=0.25)
        self.assertEqual(payload, b"ok")
        self.assertEqual(opener.call_count, 2)
        sleep.assert_called_once_with(0.25)

    def test_fetch_does_not_retry_permanent_404(self):
        error = urllib.error.HTTPError("https://example.test/missing", 404, "missing", {}, None)
        with mock.patch.object(MODULE.urllib.request, "urlopen", side_effect=error) as opener:
            with mock.patch.object(MODULE.time, "sleep") as sleep:
                with self.assertRaises(urllib.error.HTTPError):
                    MODULE.fetch("https://example.test/missing", retries=3, retry_backoff=0.01)
        self.assertEqual(opener.call_count, 1)
        sleep.assert_not_called()

    def test_total_feed_outage_preserves_state_and_notes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            (vault / "40_Sources").mkdir(parents=True)
            (vault / "state").mkdir(parents=True)
            (vault / "30_Updates").mkdir(parents=True)
            config = {
                "feeds": [{"name": "broken", "url": "https://example.test/feed"}],
                "ranking_terms": {},
                "concept_links": {},
                "required_terms_any": [],
            }
            (vault / "40_Sources" / "sources.json").write_text(json.dumps(config), encoding="utf-8")
            state_path = vault / "state" / "seen.json"
            original_state = '{"sentinel": true, "seen": {}}\n'
            state_path.write_text(original_state, encoding="utf-8")
            old_note = vault / "30_Updates" / "existing.md"
            old_note.write_text("keep me", encoding="utf-8")
            args = argparse.Namespace(
                vault=str(vault),
                config="",
                timeout=1,
                sleep=0,
                fetch_retries=3,
                retry_backoff=0,
                min_score=0,
                max_items=0,
                max_age_days=0,
                include_seen=False,
                include_old=False,
                dry_run=False,
            )
            with mock.patch.object(MODULE, "fetch", side_effect=urllib.error.URLError("offline")):
                result = MODULE.run(args)
            self.assertEqual(result, MODULE.EX_TEMPFAIL)
            self.assertEqual(state_path.read_text(encoding="utf-8"), original_state)
            self.assertEqual(old_note.read_text(encoding="utf-8"), "keep me")
            self.assertEqual(list((vault / "30_Updates").glob("* AI Embodied Intelligence Update.md")), [])

    def test_run_lock_rejects_concurrent_writer(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            first = MODULE.acquire_run_lock(vault)
            self.assertIsNotNone(first)
            second = MODULE.acquire_run_lock(vault)
            self.assertIsNone(second)
            assert first is not None
            fcntl.flock(first.fileno(), fcntl.LOCK_UN)
            first.close()
            third = MODULE.acquire_run_lock(vault)
            self.assertIsNotNone(third)
            assert third is not None
            fcntl.flock(third.fileno(), fcntl.LOCK_UN)
            third.close()


if __name__ == "__main__":
    unittest.main()
