import unittest
from solution import series_21

class TestSeries21(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(series_21(5), [1, 4, 9, 16, 25])

    def test_zero_or_negative(self):
        with self.assertRaises(ValueError):
            series_21(0)
        with self.assertRaises(ValueError):
            series_21(-5)

if __name__ == "__main__":
    unittest.main()
