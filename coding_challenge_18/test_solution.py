import unittest
from solution import display_series_18

class TestSeries18(unittest.TestCase):

    def test_series(self):
        self.assertEqual(display_series_18(9), [1, 3, 5, 7, 9])
        self.assertEqual(display_series_18(10), [1, 3, 5, 7, 9])
        self.assertEqual(display_series_18(1), [1])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            display_series_18(-5)

if __name__ == "__main__":
    unittest.main()
