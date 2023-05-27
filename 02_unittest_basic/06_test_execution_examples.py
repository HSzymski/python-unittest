import unittest


# To run only TestClass1 unit test run the following code:
# py -m unittest 06_test_execution_examples.TestClass1 -v
class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])

    # To run only test_case_2 test case run the following code:
    # py -m unittest 06_test_execution_examples.TestClass1.test_case_2 -v
    def test_case_2(self):
        self.assertTrue('apple'.islower())


class TestClass2(unittest.TestCase):

    # To run tests to the firs FAIL use the following flag: -f
    # py -m unittest 06_test_execution_examples -vf
    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['33333333', '9999999'])


class TestClass3(unittest.TestCase):

    def test_case_3(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')
