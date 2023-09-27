import unittest


def setUpModule():
    print('Set up module...')


def tearDownModule():
    print('Tear down module...')


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(f'Set up class {cls.__name__}')

    @classmethod
    def tearDownClass(cls) -> None:
        print(f'Tear down class {cls.__name__}')

    def setUp(self) -> None:
        print('Set up...')

    def tearDown(self) -> None:
        print('Tear down...')

    def test_case_1(self):
        self.assertAlmostEqual(.5+.5, 1)

    def test_case_2(self):
        self.assertAlmostEqual(.5+.5, 1)


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(.5 + .5, 1)


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(.5 + .5, 1)
