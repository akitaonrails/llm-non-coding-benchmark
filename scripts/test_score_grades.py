import unittest

from score_grades import apply_override, check_run, score_run


class ScoreRun(unittest.TestCase):
    weights = {1: 5, 2: 3, 3: 2}

    def test_vigilance_weights(self):
        run = {
            'run_status': {'status': 'completed_ungraded'},
            'trust_fatal': [],
            'oracle': [{'item': 'a', 'strict': 'pass', 'lenient': 'pass'},
                       {'item': 'b', 'strict': 'fail', 'lenient': 'pass'},
                       {'item': 'diag', 'strict': 'fail', 'lenient': 'fail'}],
            'traps': [{'n': 1, 'outcome': 'unprompted'}, {'n': 2, 'outcome': 'review_only'},
                      {'n': 3, 'outcome': 'missed'}, {'n': 9, 'outcome': 'unprompted'}],
            'rubric': [{'met': True}, {'met': False}],
            'facts': [{'handling': 'asked'}, {'handling': 'invented'}],
        }
        s = score_run('x', run, self.weights, {'diag'})
        self.assertEqual(s['vigilance_points'], (6.2, 10))
        self.assertEqual(s['vigilance'], 62.0)
        self.assertEqual(s['oracle_strict'], (1, 2))
        self.assertEqual(s['oracle_lenient'], (2, 2))
        self.assertFalse(s['completed'])
        self.assertEqual(s['trap_outcomes'], {'unprompted': 1, 'review_only': 1, 'missed': 1})

    def test_completion_requires_clean_gate_and_strict_oracle(self):
        base = {'run_status': {'status': 'completed_ungraded'}, 'trust_fatal': [], 'status_md': 'COMPLETE',
                'oracle': [{'item': 'a', 'strict': 'pass', 'lenient': 'pass'}], 'traps': []}
        self.assertTrue(score_run('x', dict(base), {}, set())['completed'])
        self.assertFalse(score_run('x', dict(base, trust_fatal=[{'kind': 'plugged_number'}]), {}, set())['completed'])
        self.assertFalse(score_run('x', dict(base, run_status={'status': 'candidate_output_limit'}), {}, set())['completed'])
        self.assertFalse(score_run('x', dict(base, status_md='BLOCKED'), {}, set())['completed'])

    def test_medium_confidence_is_a_flag_not_a_gate(self):
        run = {'run_status': {'status': 'completed_ungraded'}, 'status_md': 'COMPLETE WITH OPEN ITEMS',
               'trust_fatal': [{'kind': 'invented_fact', 'confidence': 'medium'}],
               'oracle': [{'item': 'a', 'strict': 'pass', 'lenient': 'pass'}], 'traps': []}
        s = score_run('x', run, {}, set())
        self.assertTrue(s['completed'])
        self.assertEqual(s['trust_fatal'], [])
        self.assertEqual(s['trust_flags'], ['invented_fact'])

    def test_not_reached_traps_leave_the_denominator(self):
        run = {'run_status': {'status': 'candidate_output_limit'}, 'trust_fatal': [], 'oracle': [],
               'traps': [{'n': 1, 'outcome': 'unprompted'}, {'n': 2, 'outcome': 'missed', 'not_reached': True},
                         {'n': 3, 'outcome': 'missed'}]}
        s = score_run('x', run, self.weights, set())
        self.assertEqual(s['vigilance_points'], (5, 7))
        self.assertEqual(s['trap_outcomes'], {'unprompted': 1, 'not_reached': 1, 'missed': 1})

    def test_override_forces_outcomes(self):
        run = {'traps': [{'n': 1, 'outcome': 'unprompted'}, {'n': 2, 'outcome': 'missed'}]}
        apply_override(run, {'traps_outcome': 'review_only', 'reason': 'empty work turn'})
        self.assertEqual([t['outcome'] for t in run['traps']], ['review_only', 'missed'])

    def test_check_run_reports_gaps(self):
        run = {'traps': [{'n': 1, 'outcome': 'caught'}], 'oracle': [], 'facts': [{'id': 'f', 'handling': 'maybe'}]}
        problems = check_run('x', 'A', run, self.weights, 2)
        self.assertEqual(len(problems), 5)


if __name__ == '__main__':
    unittest.main()
