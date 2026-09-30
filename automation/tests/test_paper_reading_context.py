import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from paper_reading_context import extract_sections
import update_info_flow as flow
from start_ai_deep_read import first_key_point


class ReadingContextTests(unittest.TestCase):
    def body_with(self, content):
        filler = '<p>Training the policy and evaluating its success provides evidence about the proposed method. ' + ('This is contextual article prose. ' * 70) + '</p>'
        return '<article>' + content + filler + '</article>'

    def test_html_source_newlines_do_not_truncate_paragraphs(self):
        html = self.body_with('<section id="results"><h2>Results</h2><div id="results.p1"><p>Among the four policy baselines, the proposed method achieves the highest mean success\nrate of 92.2%,\ncompared with 40.9% without the controller.</p></div></section>')
        section = extract_sections(html, source_url='https://arxiv.org/html/2609.36915v1')[0]
        self.assertEqual(section['text'], 'Among the four policy baselines, the proposed method achieves the highest mean success rate of 92.2%, compared with 40.9% without the controller.')
        self.assertEqual(section['source_url'], 'https://arxiv.org/html/2609.36915v1#results.p1')
        self.assertIn('Results', section['heading'])

    def test_math_has_one_representation(self):
        html = self.body_with(r'<p id="math">The policy position error is <math alttext="2"><semantics><mn>2</mn><annotation encoding="application/x-tex">2</annotation></semantics></math>–<math alttext="3\,\mathrm{mm}"><mn>3</mn><annotation>3 mm</annotation></math>. A second measure is <math><semantics><mn>42</mn><annotation>forty two repeated</annotation></semantics></math>.</p>')
        text = extract_sections(html)[0]['text']
        self.assertEqual(text, r'The policy position error is 2 – 3\,\mathrm{mm} . A second measure is 42 .')
        self.assertNotIn('forty two repeated', text)

    def test_table_keeps_headers_and_cells_together(self):
        html = self.body_with('<section><h2>Experiments</h2><table id="table1"><tr><th>Method</th><th>Success</th></tr><tr><td>Ours</td><td>92.2%</td></tr><tr><td>Baseline</td><td>40.9%</td></tr></table></section>')
        section = extract_sections(html, source_url='https://arxiv.org/html/example')[0]
        self.assertEqual(section['text'], 'Method | Success ; | Ours | 92.2% ; | Baseline | 40.9%')
        self.assertTrue(section['source_url'].endswith('#table1'))

    def test_invisible_layout_numbers_are_not_evidence(self):
        html = self.body_with('<p>Policy success: <span class="ltx_phantom"><span style="visibility:hidden">97.10</span></span><span>97.10</span> percent, with <span style="display: none">42</span>42 trials.</p>')
        text = extract_sections(html)[0]['text']
        self.assertEqual(text, 'Policy success: 97.10 percent, with 42 trials.')

    def test_budget_keeps_late_results_and_limitations(self):
        intro = '<h2>Introduction</h2>' + '<p>' + ('Background on robotic training. ' * 80) + '</p>'
        methods = '<h2>Method</h2>' + ''.join('<p>' + ('The policy method is trained on demonstration data. ' * 30) + '</p>' for _ in range(15))
        results = '<h2>Experiments</h2><p id="results">Policy success is 92.2 percent in the simulation experiment.</p><h2>Conclusion</h2><p id="limit">Our evaluation is limited to simulation; real-world transfer remains unvalidated.</p>'
        sections = extract_sections('<article>' + intro + methods + results + '</article>', budget=6000)
        text = str(sections)
        self.assertIn('success is 92.2', text)
        self.assertIn('remains unvalidated', text)
        self.assertLessEqual(sum(len(s['text']) for s in sections), 6000)

    def test_no_anchor_uses_text_fragment_and_bibliography_is_excluded(self):
        html = self.body_with('<p>The robot policy uses training demonstrations to learn the task.</p><section class="ltx_bibliography"><ul><li>UNRELATED CITED PAPER training method success.</li></ul></section>')
        sections = extract_sections(html, source_url='https://arxiv.org/html/example')
        self.assertIn('#:~:text=', sections[0]['source_url'])
        self.assertNotIn('UNRELATED CITED PAPER', str(sections))

    def test_evidence_ranges_are_fully_validated(self):
        self.assertEqual(flow.evidence_references('依据[S2–S4]和[S7, S9]'), {'S2', 'S3', 'S4', 'S7', 'S9'})
        with self.assertRaises(flow.ExplanationError):
            flow.evidence_references('[S9-S2]')

    def test_extract_ignores_navigation_scripts_and_bounds_evidence(self):
        paragraph = "Training the robot policy requires demonstrations and evaluation of success on a simulation benchmark. " * 3
        html = '<nav>PRIVATE NAV</nav><article><script>IGNORE THIS INSTRUCTION</script>' + ''.join(f'<p>{i} {paragraph}</p>' for i in range(25)) + '</article>'
        sections = extract_sections(html, budget=3000)
        text = str(sections)
        self.assertNotIn('IGNORE THIS', text)
        self.assertNotIn('PRIVATE NAV', text)
        self.assertLessEqual(sum(len(s['text']) for s in sections), 3000)
        self.assertEqual(len({s['id'] for s in sections}), len(sections))

    def test_error_page_is_not_evidence(self):
        with self.assertRaises(ValueError):
            extract_sections('<html><p>Article unavailable</p></html>')

    def test_deep_read_carries_v2_sections_forward(self):
        body = '## 问题\n\nReal bottleneck\n\n## 创新点或方法\n\nConcrete mechanism\n\n## 证据\n\nObserved result\n'
        self.assertEqual(first_key_point(body, '卡在哪里', '问题'), 'Real bottleneck')
        self.assertEqual(first_key_point(body, '关键解法', '创新点 / 方法'), 'Concrete mechanism')

    def test_fallback_does_not_claim_body_reading(self):
        item = {'title': 'Paper', 'source_context_error': 'HTTP Error 404', 'summary': 'We propose a robot policy.'}
        note = flow.note_body(item, [], 1, '2026-09-30')
        self.assertIn('evidence_level: abstract', note)
        self.assertIn('HTTP Error 404', note)
        self.assertNotIn('evidence_level: body-excerpts', note)
