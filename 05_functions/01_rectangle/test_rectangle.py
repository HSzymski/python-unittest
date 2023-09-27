import unittest
from .rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'additional message')

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_type_should_raise_error(self):
        with self.assertRaises(ValueError):
            area(-4, 5)
        with self.assertRaises(ValueError):
            area(4, -5)

class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18, 'Perimiters not equal')

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 4, '5')

    def test_perimeter_negative_type_should_raise_error(self):
        with self.assertRaises(ValueError):
            perimeter(-4, 5)
        with self.assertRaises(ValueError):
            perimeter(4, -5)
