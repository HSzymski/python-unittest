import unittest


def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'additional message')

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_type_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)

        with self.assertRaises(ValueError):
            area(4, -5)
# running by executing in terminal following commands:
# - python -m unittest .\03_run_with_unittest.py
# - py -m unittest .\03_run_with_unittest.py
# - py -m unittest .\03_run_with_unittest.py -v
