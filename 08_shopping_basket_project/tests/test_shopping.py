import unittest
from shopping.basket import ShoppingBasket


class TestShoppingBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Setting up basket without any product.')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(self.basket.get_product(0), IndexError)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total, 0)


class TestShoppingBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Setting up basket without any product.')
        cls.basket = ShoppingBasket() \
            .add_product('milk', 3.)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_total_amount_should_have_tax(self):
        cases = ([10, 3.3],
                 [21, 3.63])
        for tax, results in cases:
            with self.subTest(cases=cases):
                self.assertAlmostEqual(self.basket.total(tax), results)

    def test_getting_product(self):
        self.assertIsEqual('milk', self.basket.get_product(0).name)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(self.basket.get_product(1), IndexError)


class TestShoppingBasketWithManyProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Setting up basket without any product.')
        cls.basket = ShoppingBasket() \
            .add_product('milk', 3.) \
            .add_product('water', 2.) \
            .add_product('water', 2.)

    def test_size_of_basket_should_be_two(self):
        self.assertEqual(len(self.basket), 2)

    def test_order_of_product(self):
        self.assertEqual('milk', self.basket.get_product(0).name)
        self.assertEqual(3., self.basket.get_product(0).price)

        self.assertEqual('water', self.basket.get_product(1).name)
        self.assertEqual(2., self.basket.get_product(1).price)

        self.assertEqual('water', self.basket.get_product(2).name)
        self.assertEqual(2., self.basket.get_product(2).price)

    def test_total_amount_should_have_tax(self):
        cases = ([10, 7.7],
                 [21, 8.61])
        for tax, results in cases:
            with self.subTest(cases=cases):
                self.assertAlmostEqual(self.basket.total(tax), results)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(self.basket.get_product(3), IndexError)

