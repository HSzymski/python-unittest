import unittest
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    # in that case in the console we will have information only of the first failed assert case
    # def test_add(self):
    #     self.assertEqual(self.calc.add(-3, -2), -5)
    #     self.assertEqual(self.calc.add(-3, 2), -1)
    #     self.assertEqual(self.calc.add(3, -2), 0)
    #     self.assertEqual(self.calc.add(3, 2), 5)

    # in that case in the console we will have information about all failed assert cases
    def test_add(self):
        cases = [
            (-3, -2, -5),
            (-3, 2, -1),
            (3, -2, 0),
            (3, 2, 6)
        ]
        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.calc.add(x, y), result)

