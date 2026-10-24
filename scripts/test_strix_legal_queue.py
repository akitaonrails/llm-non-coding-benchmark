import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from run_strix_legal_queue import CASE, handle_pending, legal_decision, unload


class LegalControllerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.run = Path(self.temp.name)
        self.case = self.run / CASE
        self.folder = self.case / 'work/workspace/deliverable'
        self.folder.mkdir(parents=True)
        self.expected = [{'when': 'se prazos.json disser prazo_em_dobro = false', 'message': 'fixed'}]
        self.pending = {'case': CASE, 'session': 1, 'pushbacks': self.expected}
        self.write(False)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, value):
        (self.folder / 'prazos.json').write_text(json.dumps({'citacao': {'prazo_em_dobro': value}}))
        for name in ['memoria.md', 'STATUS.md']:
            (self.folder / name).write_text('present')

    def test_false_selects_only_scripted_pushback(self):
        decision = legal_decision(self.case, self.pending, self.expected)
        self.assertEqual(decision['pushback_indices'], [0])
        self.assertFalse(decision['nudge'])

    def test_true_selects_no_pushback(self):
        self.write(True)
        self.assertEqual(legal_decision(self.case, self.pending, self.expected)['pushback_indices'], [])

    def test_string_false_requires_manual_review(self):
        self.write('false')
        self.assertIsNone(legal_decision(self.case, self.pending, self.expected))

    def test_missing_artifact_requires_manual_review(self):
        (self.folder / 'STATUS.md').unlink()
        self.assertIsNone(legal_decision(self.case, self.pending, self.expected))

    def test_changed_script_requires_manual_review(self):
        self.assertIsNone(legal_decision(self.case, {**self.pending, 'pushbacks': []}, self.expected))

    def test_symlink_outside_workspace_is_rejected(self):
        path = self.folder / 'memoria.md'
        path.unlink()
        outside = self.run / 'outside.md'
        outside.write_text('not a candidate artifact')
        path.symlink_to(outside)
        self.assertIsNone(legal_decision(self.case, self.pending, self.expected))

    def test_client_questions_are_never_answered(self):
        path = self.case / '01-client.pending.json'
        path.write_text(json.dumps({'questions': 'Is it electronic?', 'facts': []}))
        self.assertEqual(handle_pending(self.run, self.expected), [str(path)])
        self.assertFalse((self.case / '01-client.decision.json').exists())

    def test_automatic_decision_is_atomic_and_never_overwritten(self):
        (self.case / 's1.pending.json').write_text(json.dumps(self.pending))
        self.assertEqual(handle_pending(self.run, self.expected), [])
        target = self.case / 's1.decision.json'
        first = target.read_text()
        self.write(True)
        handle_pending(self.run, self.expected)
        self.assertEqual(target.read_text(), first)
        self.assertFalse(list(self.case.glob('*.queue-tmp')))

    @patch('run_strix_legal_queue.urllib.request.urlopen')
    def test_unload_never_touches_unrelated_model_or_swap_service(self, request):
        with self.assertRaises(ValueError):
            unload({'endpoint': 'http://192.168.0.90:11434', 'model': 'nomic-embed-text:latest'})
        unload({'endpoint': 'http://192.168.0.90:11435', 'model': 'glm-4.7-flash:q8'})
        request.assert_not_called()


if __name__ == '__main__':
    unittest.main()
