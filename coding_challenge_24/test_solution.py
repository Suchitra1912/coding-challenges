import unittest
from solution import series_24

class TestSeries24(unittest.TestCase):

    def test_fibonacci_series(self):
        self.assertEqual(series_24(5), [1, 1, 2, 3, 5])
        with self.assertRaises(ValueError):
            series_24(0)

if __name__ == "__main__":
    unittest.main()
