import unittest
from unittest.mock import patch
from code_generator import get_code, get_today_name, get_code_with_day


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_should_return_3(self, mocked_random):
        mocked_random.return_value = 3
        actual = get_code()
        expected = 'XC-3'

        self.assertEqual(actual, expected)

    @patch('random.randint')
    def test_get_code_mock_should_return_5(self, mocked_random):
        mocked_random.return_value = 5
        actual = get_code()
        expected = 'XC-5'

        self.assertEqual(actual, expected)


class TestGetCodeWithDay(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_with_day_with_today_date(self, mock_int):
        # wrong way to write the test, result depends on the date
        mock_int.return_value = 5
        actual = get_code_with_day()
        expected = 'XC-5-Wed'

        self.assertEqual(actual, expected)

    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_friday(self, mock_int, mock_day):
        mock_int.return_value = 5
        mock_day.return_value = 'Fri'
        actual = get_code_with_day()
        expected = 'XC-5-Fri'

        self.assertEqual(actual, expected)

    @patch('code_generator.get_today_name')
    @patch('code_generator.get_code')
    def test_get_code_with_day_with_mocked_friday(self, mock_code, mock_day):
        mock_code.return_value = 'XC-5'
        mock_day.return_value = 'Fri'
        actual = get_code_with_day()
        expected = 'XC-5-Fri'

        self.assertEqual(actual, expected)

    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_sunday(self, mock_int, mock_day):
        mock_int.return_value = 7
        mock_day.return_value = 'Sun'
        actual = get_code_with_day()
        expected = 'XC-7-Sun'

        self.assertEqual(actual, expected)
