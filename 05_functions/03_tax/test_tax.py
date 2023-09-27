import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_different_age_value(self):
        self.assertAlmostEqual(calc_tax(10 ** 4, .1, 18), 1000)
        self.assertAlmostEqual(calc_tax(10 ** 6, .1, 18), 5000)
        self.assertAlmostEqual(calc_tax(10 ** 4, .1, 19), 1000)
        self.assertAlmostEqual(calc_tax(10 ** 6, .1, 19), 100000)
        self.assertAlmostEqual(calc_tax(10 ** 4, .15, 66), 1500)
        self.assertAlmostEqual(calc_tax(10 ** 6, .15, 66), 8000)

    def test_calc_tax_with_incorrect_amount_type_should_raise_error(self):
        with self.assertRaises(TypeError):
            calc_tax('ten', .23, 20)

    def test_calc_tax_with_incorrect_tax_rate_type_should_raise_error(self):
        with self.assertRaises(TypeError):
            calc_tax(100, '.23', 20)

    def test_calc_tax_with_incorrect_age_type_should_raise_error(self):
        with self.assertRaises(TypeError):
            calc_tax(100, .1, {'1': 'a'})

    def test_calc_tax_with_incorrect_age_value_should_raise_error(self):
        with self.assertRaises(ValueError):
            calc_tax(100, .1, -1)
