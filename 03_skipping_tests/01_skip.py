import unittest
import sys
from datetime import date


class TestClass(unittest.TestCase):

    @unittest.skip('Skipping test due to some reason.')
    def test_case_skip(self):
        self.assertEqual('a'.upper(), 'A')

    @unittest.skipIf(date.today().day % 2 != 0, 'Skipping odd days.')
    def test_case_skip_odd_days(self):
        self.assertEqual(date.today().day % 2, 0)

    @unittest.skipIf((sys.version_info[0] == 3) & (sys.version_info[1] <= 10),
                     'Skipping, Python version lower than 3.10')
    def test_case_skip_python_ver_lower_than_3_10(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows.')
    def test_requires_windows(self):
        self.assertAlmostEqual(0.1+0.2, 0.3, 5)
