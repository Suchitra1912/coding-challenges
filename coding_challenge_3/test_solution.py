import unittest
from solution import calculate_discount

class TestDiscountCalculator(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_discount(2000, 10), 200.00)
        self.assertEqual(calculate_discount(500, 25), 125.00)

    def test_zero_values(self):
        self.assertEqual(calculate_discount(0, 10), 0.00)
        self.assertEqual(calculate_discount(1000, 0), 0.00)
        self.assertEqual(calculate_discount(0, 0), 0.00)

    def test_edge_cases(self):
        self.assertEqual(calculate_discount(1e6, 0.01), 100.00)
        self.assertEqual(calculate_discount(1234.56, 12.5), 154.32)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_discount(-1000, 10)
        with self.assertRaises(ValueError):
            calculate_discount(1000, -10)
        with self.assertRaises(ValueError):
            calculate_discount(-1000, -10)

if __name__ == "__main__":
    unittest.main()
