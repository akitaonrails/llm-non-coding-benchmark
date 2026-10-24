"""Controller tests; no model calls."""
import unittest
from run_codex_baseline import match_facts


class ClientMatching(unittest.TestCase):
    def setUp(self):
        self.facts = [dict(id='april', trigger=['pró-labore de abril'], answer='paid'),
                      dict(id='rent', trigger=['locação'], answer='notebooks')]

    def test_only_requested_fact_released(self):
        self.assertEqual([f['id'] for f in match_facts('O PRO-LABORE DE ABRIL foi pago?', self.facts, set())], ['april'])

    def test_unrelated_question_does_not_reveal(self):
        self.assertEqual(match_facts('What is the revenue?', self.facts, set()), [])

    def test_previously_released_fact_is_not_repeated(self):
        self.assertEqual(match_facts('pró-labore de abril?', self.facts, {'april'}), [])


if __name__ == '__main__':
    unittest.main()
