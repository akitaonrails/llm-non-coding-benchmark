import unittest

from verify_full_suite import preserved_in_retries


class PreservedMatching(unittest.TestCase):
    def test_exact_entry(self):
        retries = [{'preserved': '_aborted/brlaw_03_pejotizacao-attempt2'}]
        self.assertTrue(preserved_in_retries('brlaw_03_pejotizacao-attempt2', retries))
        self.assertFalse(preserved_in_retries('brlaw_03_pejotizacao-attempt3', retries))

    def test_wildcard_batch_entry(self):
        retries = [{'preserved': '_aborted/usacc_02_close_gap-attempt*'}]
        self.assertTrue(preserved_in_retries('usacc_02_close_gap-attempt3', retries))
        self.assertFalse(preserved_in_retries('usacc_03_household_1040-attempt3', retries))

    def test_entry_without_preserved(self):
        self.assertFalse(preserved_in_retries('x-attempt1', [{'case': 'x', 'reason': 'note'}]))


if __name__ == '__main__':
    unittest.main()
