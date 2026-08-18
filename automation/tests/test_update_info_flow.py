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
    def test_abstract_summary_is_compact_and_evidence_bounded(self):
        abstract = (
            "Robot policies fail in cluttered scenes. "
            "We propose a contact-aware diffusion controller. "
            "Results show a 17% success-rate improvement on three benchmarks. "
            "However, the method does not handle deformable objects."
        )
        summary = MODULE.summarize_abstract(abstract)
        self.assertIn("contact-aware", summary["method"])
        self.assertIn("17%", summary["evidence"])
        self.assertIn("does not handle", summary["limitation"])
        self.assertFalse(summary["needs_fulltext"])

    def test_abstract_summary_marks_unreported_evidence(self):
        summary = MODULE.summarize_abstract("We propose a compact robot policy for mobile manipulation.")
        self.assertEqual(summary["evidence"], MODULE.UNSTATED_EVIDENCE)
        self.assertEqual(summary["limitation"], MODULE.UNSTATED_LIMITATION)
        self.assertTrue(summary["needs_fulltext"])

    def test_note_and_digest_use_decision_first_format(self):
        items = []
        for index in range(15):
            abstract = f"We propose controller {index}. Results show a {index + 1}% gain."
            item = {
                "title": f"Paper {index}",
                "source": "arXiv",
                "url": f"https://example.test/{index}",
                "published": "2026-08-12T00:00:00Z",
                "age_days": 0,
                "authors": ["A. Author"],
                "summary": abstract,
                "score": 20 - index,
                "concepts": ["机器人学习"],
                "link_path": f"30_Updates/2026-08-12/Paper {index}",
                "compact_summary": MODULE.summarize_abstract(abstract),
            }
            items.append(item)
        note = MODULE.note_body(items[0], items[0]["concepts"], items[0]["score"], "2026-08-12")
        self.assertIn("format_version: 2", note)
        self.assertIn("## 关键点", note)
        self.assertIn("**创新点 / 方法**", note)
        self.assertIn("<summary>原始摘要与来源</summary>", note)
        self.assertIn("[[AI 论文深读工作流|", note)
        self.assertIn("scripts/start_ai_deep_read.py", note)
        self.assertNotIn("## 我的判断", note)

        digest = MODULE.digest_body("2026-08-12", items, 100, [], "机器人学习 15", 0)
        self.assertIn("## 必读 5 篇", digest)
        self.assertIn("## 扫读 7 篇", digest)
        self.assertIn("## 其余存档 3 篇", digest)
        self.assertIn("[[AI 论文深读工作流|", digest)
        for item in items:
            self.assertIn(item["link_path"], digest)

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

    def test_source_falls_back_to_official_feed_after_primary_429(self):
        rss = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel><item>
    <title>Fallback Robot Paper</title>
    <link>https://arxiv.org/abs/2608.00001</link>
    <description>Abstract: We propose a real robot policy.</description>
    <pubDate>Mon, 17 Aug 2026 00:00:00 -0400</pubDate>
    <dc:creator>A. Author</dc:creator>
  </item></channel>
</rss>"""
        rate_error = urllib.error.HTTPError(
            "https://export.arxiv.org/api/query", 429, "Too Many Requests", {}, None
        )
        source = {
            "name": "arXiv frontier",
            "url": "https://export.arxiv.org/api/query",
            "fallback_urls": ["https://rss.arxiv.org/rss/cs.RO"],
            "fetch_retries": 1,
            "fallback_fetch_retries": 2,
            "weight": 6,
            "max_age_days": 21,
        }
        with mock.patch.object(MODULE, "fetch", side_effect=[rate_error, rss]) as fetcher:
            with mock.patch.object(MODULE.time, "sleep") as sleep:
                items, recovery, failure = MODULE.fetch_source(
                    source,
                    timeout=10,
                    retries=3,
                    retry_backoff=2,
                    inter_fetch_sleep=3,
                )
        self.assertEqual([item["title"] for item in items], ["Fallback Robot Paper"])
        self.assertIn("recovered via 1/1", recovery)
        self.assertEqual(failure, "")
        self.assertEqual(fetcher.call_count, 2)
        sleep.assert_called_once_with(3)

    def test_run_records_recovered_source_in_state_and_digest(self):
        rss = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel><item>
    <title>Recovered Real Robot Paper</title>
    <link>https://arxiv.org/abs/2608.00002</link>
    <description>We propose a real robot policy. Results show a 20% gain.</description>
    <pubDate>Mon, 17 Aug 2026 00:00:00 -0400</pubDate>
    <dc:creator>B. Author</dc:creator>
  </item></channel>
</rss>"""
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            (vault / "40_Sources").mkdir(parents=True)
            (vault / "state").mkdir(parents=True)
            config = {
                "feeds": [
                    {
                        "name": "critical papers",
                        "url": "https://example.test/primary",
                        "fallback_urls": ["https://example.test/fallback"],
                        "critical": True,
                        "fetch_retries": 1,
                        "fallback_fetch_retries": 1,
                        "weight": 6,
                    }
                ],
                "ranking_terms": {"robot": 5},
                "concept_links": {"机器人学习": ["robot"]},
                "required_terms_any": ["robot"],
                "min_score": 1,
                "max_items_per_run": 5,
            }
            (vault / "40_Sources" / "sources.json").write_text(
                json.dumps(config), encoding="utf-8"
            )
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
            with mock.patch.object(
                MODULE,
                "fetch",
                side_effect=[urllib.error.URLError("rate limited"), rss],
            ):
                result = MODULE.run(args)

            self.assertEqual(result, 0)
            state = json.loads((vault / "state" / "seen.json").read_text(encoding="utf-8"))
            self.assertEqual(state["last_failures"], [])
            self.assertEqual(len(state["last_recoveries"]), 1)
            self.assertEqual(state["last_selected_count"], 1)
            digest = Path(state["last_output_path"]).read_text(encoding="utf-8")
            self.assertIn("- **源异常**：1", digest)
            self.assertIn("- 自动恢复信息源：1", digest)

    def test_critical_source_failure_blocks_partial_digest(self):
        rss = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><item>
  <title>Generic robot story</title>
  <link>https://example.test/story</link>
  <description>A robot story without the paper source.</description>
  <pubDate>Mon, 17 Aug 2026 00:00:00 +0000</pubDate>
</item></channel></rss>"""
        with tempfile.TemporaryDirectory() as temp_dir:
            vault = Path(temp_dir)
            (vault / "40_Sources").mkdir(parents=True)
            (vault / "state").mkdir(parents=True)
            (vault / "30_Updates").mkdir(parents=True)
            config = {
                "feeds": [
                    {
                        "name": "critical papers",
                        "url": "https://example.test/critical",
                        "critical": True,
                    },
                    {"name": "generic news", "url": "https://example.test/news"},
                ],
                "ranking_terms": {"robot": 5},
                "concept_links": {},
                "required_terms_any": ["robot"],
            }
            (vault / "40_Sources" / "sources.json").write_text(
                json.dumps(config), encoding="utf-8"
            )
            state_path = vault / "state" / "seen.json"
            original_state = '{"sentinel": true, "seen": {}}\n'
            state_path.write_text(original_state, encoding="utf-8")
            args = argparse.Namespace(
                vault=str(vault),
                config="",
                timeout=1,
                sleep=0,
                fetch_retries=1,
                retry_backoff=0,
                min_score=0,
                max_items=0,
                max_age_days=0,
                include_seen=False,
                include_old=False,
                dry_run=False,
            )

            def fake_fetch(url, **kwargs):
                if url.endswith("critical"):
                    raise urllib.error.URLError("offline")
                return rss

            with mock.patch.object(MODULE, "fetch", side_effect=fake_fetch):
                result = MODULE.run(args)
            self.assertEqual(result, MODULE.EX_TEMPFAIL)
            self.assertEqual(state_path.read_text(encoding="utf-8"), original_state)
            self.assertEqual(
                list((vault / "30_Updates").glob("* AI Embodied Intelligence Update.md")),
                [],
            )

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
