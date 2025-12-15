import unittest
from solution import display_series_20

class TestSeries20(unittest.TestCase):

    def test_series(self):
        self.assertEqual(display_series_20(7), [1, 2, 4, 7, 11, 16, 22])
        self.assertEqual(display_series_20(1), [1])
        self.assertEqual(display_series_20(4), [1, 2, 4, 7])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            display_series_20(0)
        with self.assertRaises(ValueError):
            display_series_20(-2)

if __name__ == "__main__":
    unittest.main()
