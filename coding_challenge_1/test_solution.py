import unittest
import math
from solution import sum_and_average

class TestSumAndAverage(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_and_average(10, 20), (30, 15))
        self.assertEqual(sum_and_average(100, 200), (300, 150))

    def test_negative_numbers(self):
        self.assertEqual(sum_and_average(-5, -15), (-20, -10))
        self.assertEqual(sum_and_average(-10, 5), (-5, -2.5))

    def test_zero(self):
        self.assertEqual(sum_and_average(0, 0), (0, 0))
        self.assertEqual(sum_and_average(0, 10), (10, 5))

    def test_floats(self):
        self.assertEqual(sum_and_average(2.5, 7.5), (10.0, 5.0))
        self.assertEqual(sum_and_average(-3.5, 3.5), (0.0, 0.0))

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            sum_and_average("10", 5)
        with self.assertRaises(ValueError):
            sum_and_average(10, None)
        with self.assertRaises(ValueError):
            sum_and_average([], 5)

    def test_nan(self):
        with self.assertRaises(ValueError):
            sum_and_average(math.nan, 10)
        with self.assertRaises(ValueError):
            sum_and_average(10, math.nan)

    def test_infinity(self):
        with self.assertRaises(ValueError):
            sum_and_average(float("inf"), 10)
        with self.assertRaises(ValueError):
            sum_and_average(10, float("-inf"))

if __name__ == "__main__":
    unittest.main()
