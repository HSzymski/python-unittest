import unittest
from tax import calc_tax, calc_tax_2


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_10_percent(self):
        self.assertEqual(10, calc_tax(100, 10))

    def test_calc_tax_with_14_percent(self):
        # assertEqual will rise an error!
        self.assertEqual(14, calc_tax(100, 14))

    def test_calc_tax_with_14_percent_with_almost_equal(self):
        # assertEqual will rise an error!
        self.assertAlmostEqual(14, calc_tax(100, 14))


class TestCalcTax2(unittest.TestCase):

    def test_calc_tax_with_10_percent(self):
        self.assertAlmostEqual(10, calc_tax_2(100, .1))

    def test_calc_tax_with_14_percent_with_almost_equal(self):
        # assertEqual will rise an error!
        self.assertAlmostEqual(14, calc_tax_2(100, .14))

    def test_calc_tax_with_incorrect_amount_type_should_raise_error(self):
        with self.assertRaises(TypeError):
            calc_tax_2('ten', .23)

    def test_calc_tax_with_incorrect_tax_rate_type_should_raise_error(self):
        with self.assertRaises(TypeError):
            calc_tax_2(100, '.23')

    def test_calc_tax_with_incorrect_tax_rate_should_raise_error(self):
        with self.assertRaises(ValueError):
            calc_tax_2(100, 0)
            calc_tax_2(100, 1)
