import unittest
from solution import calculate_tax_on_purchase

class TestTaxOnPurchase(unittest.TestCase):

    def test_low_tax(self):
        tax, total = calculate_tax_on_purchase(3000)
        self.assertEqual(tax, 150.0)        # 5% of 3000
        self.assertEqual(total, 3150.0)

    def test_medium_tax(self):
        tax, total = calculate_tax_on_purchase(10000)
        self.assertEqual(tax, 1000.0)       # 10% of 10000
        self.assertEqual(total, 11000.0)

    def test_high_tax(self):
        tax, total = calculate_tax_on_purchase(30000)
        self.assertEqual(tax, 4500.0)       # 15% of 30000
        self.assertEqual(total, 34500.0)

if __name__ == "__main__":
    unittest.main()
