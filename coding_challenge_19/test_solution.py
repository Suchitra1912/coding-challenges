import unittest
from solution import display_series_19

class TestSeries19(unittest.TestCase):

    def test_series(self):
        self.assertEqual(display_series_19(8), [4, 16, 36, 64])
        self.assertEqual(display_series_19(10), [4, 16, 36, 64, 100])
        self.assertEqual(display_series_19(2), [4])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            display_series_19(-3)

if __name__ == "__main__":
    unittest.main()
