import json
import tempfile
import unittest
from pathlib import Path

from report_full_coverage import coverage


class CoverageTests(unittest.TestCase):
    def test_subset_manifest_cannot_count_as_full_completion(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'manifest.json').write_text(json.dumps({'cases': ['a']}))
            r = coverage(p, ['a', 'b'], {'a': 1, 'b': 1})
            self.assertFalse(r['all_cases_accounted_for'])
            self.assertTrue(r['errors'])

    def test_failed_case_is_accounted_for_but_not_completed(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'manifest.json').write_text(json.dumps({'cases': ['a']}))
            (p / 'a').mkdir()
            (p / 'a/result.json').write_text(json.dumps({'status': 'candidate_output_limit'}))
            r = coverage(p, ['a'], {'a': 3})
            self.assertTrue(r['all_cases_accounted_for'])
            self.assertFalse(r['all_cases_completed'])
            self.assertEqual(r['completed_initial_sessions'], 0)

    def test_missing_session_prevents_full_completion(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'manifest.json').write_text(json.dumps({'cases': ['a']}))
            (p / 'a').mkdir()
            (p / 'a/result.json').write_text(json.dumps({'status': 'completed_ungraded'}))
            turns = [{'label': 's1-work', 'complete': True},
                     {'label': 'review', 'complete': True}]
            f = p / 'a/turns.json'
            f.write_text(json.dumps(turns))
            self.assertFalse(coverage(p, ['a'], {'a': 2})['all_cases_completed'])
            turns.append({'label': 's2-work', 'complete': True})
            f.write_text(json.dumps(turns))
            self.assertTrue(coverage(p, ['a'], {'a': 2})['all_cases_completed'])


if __name__ == '__main__':
    unittest.main()
