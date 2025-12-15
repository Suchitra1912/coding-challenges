import unittest
from solution import calculate_loyalty_points

class TestLoyaltyPoints(unittest.TestCase):

    def test_zero_total(self):
        self.assertEqual(calculate_loyalty_points(0), 0)

    def test_positive_totals(self):
        # Normal cases
        self.assertEqual(calculate_loyalty_points(50), 0)      # Less than 100
        self.assertEqual(calculate_loyalty_points(250), 2)
        self.assertEqual(calculate_loyalty_points(999), 9)
        self.assertEqual(calculate_loyalty_points(1000), 10)

    def test_large_totals(self):
        # Edge cases for very large totals
        self.assertEqual(calculate_loyalty_points(1000000), 10000)
        self.assertEqual(calculate_loyalty_points(1234567), 12345)

    def test_negative_total(self):
        with self.assertRaises(ValueError):
            calculate_loyalty_points(-100)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_loyalty_points("1000")
        with self.assertRaises(TypeError):
            calculate_loyalty_points(None)

if __name__ == "__main__":
    unittest.main()
