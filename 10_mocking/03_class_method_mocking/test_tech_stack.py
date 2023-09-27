import unittest
from unittest.mock import patch
from tech_stack import TechStack


class TestTechStack(unittest.TestCase):

    def setUp(self) -> None:
        print('Setting up...')
        self.stack = TechStack()
        self.stack.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_sql(self, mocked_method):
        mocked_method.return_value = 'sql'
        expected = 'sql'
        actual = self.stack.get_tech()

        self.assertEqual(actual, expected)

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_python(self, mocked_method):
        mocked_method.return_value = 'python'
        expected = 'python'
        actual = self.stack.get_tech()

        self.assertEqual(actual, expected)
