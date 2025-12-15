import unittest
from solution import apply_discounts

class TestApplyDiscounts(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(apply_discounts(5000, 10), 5000)

    def test_amount_discount(self):
        self.assertEqual(apply_discounts(15000, 10), 13500.0)

    def test_quantity_discount(self):
        self.assertEqual(apply_discounts(9000, 25), 8550.0)

    def test_both_discounts(self):
        self.assertEqual(apply_discounts(20000, 30), 17100.0)

if __name__ == "__main__":
    unittest.main()
