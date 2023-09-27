import unittest


def setUpModule():
    print('Set up module...')


def tearDownModule():
    print('Tear down module...')


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(.5+.5, 1)


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(.5 + .5, 1)
