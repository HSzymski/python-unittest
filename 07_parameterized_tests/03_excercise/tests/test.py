import unittest
from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)

    def test_area_incorrect_value_should_raise_value_error(self):
        cases = [
            (-4, 5),
            (4, -5),
            (10, 0)
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(ValueError, area, width, height)


class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        cases = [
            (1, 5, 12),
            (2, 10, 24),
            (100, 50, 300)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(perimeter(width, height), result)

    def test_perimeter_incorrect_type_should_raise_type_error(self):
        cases = [
            (4, '5'),
            ('2', 8),
            ('two', 'three')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, perimeter, width, height)

    def test_perimeter_incorrect_value_should_raise_value_error(self):
        cases = [
            (-40, 5),
            (4, -10),
            (0, 0)
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(ValueError, perimeter, width, height)
