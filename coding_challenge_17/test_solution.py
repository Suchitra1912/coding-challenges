import unittest
from solution import display_series_17

class TestSeries17(unittest.TestCase):

    def test_series(self):
        self.assertEqual(display_series_17(5), [1, 2, 3, 4, 5])
        self.assertEqual(display_series_17(1), [1])

    def test_invalid_input(self):
        # Check that ValueError is raised for invalid input
        with self.assertRaises(ValueError):
            display_series_17(0)
        with self.assertRaises(ValueError):
            display_series_17(-1)

if __name__ == "__main__":
    unittest.main()
