import unittest
from ..excercise.solution import (map_longest, filter_ge_four_char, factorial, count_string, remove_duplicates,
                                  is_distinct, Laptop)


class TestMapLongest(unittest.TestCase):

    def test_map_longest_should_be_six(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest(['sql', 'r', 'python']), 6, msg)

    def test_map_longest_should_be_three(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest(['sql', 'r']), 3, msg)

    def test_map_longest_should_be_zero(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest([]), 0, msg)


class TestFilterGeFourChar(unittest.TestCase):

    def test_filter_ge_four_char_with_one_item(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char(['sql', 'r', 'java'])
        expected = ['java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_with_two_item(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char(['sql', 'r', 'python', 'java'])
        expected = ['python', 'java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_should_be_empty(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char([])
        expected = []
        self.assertEqual(actual, expected, msg)


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        msg = 'Popraw implementację funkcji factorial().'
        self.assertEqual(factorial(0), 1, msg)
        self.assertEqual(factorial(1), 1, msg)
        self.assertEqual(factorial(2), 2, msg)
        self.assertEqual(factorial(3), 6, msg)
        self.assertEqual(factorial(6), 720, msg)


class TestCountString(unittest.TestCase):

    def test_count_string_empty_list(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string([]), 0, msg)

    def test_count_string_without_string(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string([1, 2]), 0, msg)

    def test_count_string_with_three_string(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string(['c++', 3, 'c', 'java']), 3, msg)


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        self.assertEqual(remove_duplicates([]), [], msg)

    def test_remove_duplicates_without_string(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        self.assertEqual(remove_duplicates([3, 3, 1]), [1, 3], msg)

    def test_remove_duplicates_with_three_string(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        actual = sorted(remove_duplicates(['c++', 'c', 'c']))
        expected = ['c', 'c++']
        self.assertEqual(actual, expected, msg)


class TestIsDistinct(unittest.TestCase):

    def test_is_distinct_empty_list(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([]), True, msg)

    def test_is_distinct_with_numbers_should_return_false(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([3, 3, 1]), False, msg)

    def test_is_distinct_with_numbers_should_return_true(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([3, 2, 1]), True, msg)

    def test_is_distinct_with_strings(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct(['c++', 'c', 'r']), True, msg)


class TestLaptop(unittest.TestCase):

    def setUp(self):
        self.laptop = Laptop('Acer', 'Predator', 5490)

    def test_laptop_has_brand_instance_attr(self):
        msg = 'Brak atrybutu instancji brand.'
        self.assertTrue(hasattr(self.laptop, 'brand'), msg)

    def test_laptop_has_model_instance_attr(self):
        msg = 'Brak atrybutu instancji model.'
        self.assertTrue(hasattr(self.laptop, 'model'), msg)

    def test_laptop_has_price_instance_attr(self):
        msg = 'Brak atrybutu instancji price.'
        self.assertTrue(hasattr(self.laptop, 'price'), msg)

    def test_laptop_has_three_instance_attrs(self):
        msg = 'Nie zdefiniowano dokładnie trzech atrybutów instancji.'
        actual = len([attr for attr in dir(self.laptop)
                      if not attr.startswith('_')])
        expected = 3
        self.assertEqual(actual, expected, msg)

    def test_laptop_incorrect_brand_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 200, 'Predator', 1000)
        self.assertRaises(TypeError, Laptop, True, 'Predator', 1000)

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', -1000)
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', 0)

    def test_laptop_has_name_property(self):
        msg = 'Class Laptop do not have price attribute.'
        self.assertTrue(hasattr(Laptop, 'price'), msg)
        self.assertIsInstance(Laptop.price, property)

    def test_person_repr_method(self):
        msg = 'Repair laptop instance __repr__().'
        actual = repr(self.laptop)
        expected = "Laptop(brand='Acer', model='Predator')"
        self.assertEqual(actual, expected, msg)
