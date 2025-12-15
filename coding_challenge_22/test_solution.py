import unittest
from solution import series_22

class TestSeries22(unittest.TestCase):
    def test_series_generation(self):
        self.assertEqual(series_22(5), [1, 4, 7, 11, 18])
        self.assertEqual(series_22(1), [1])
        self.assertEqual(series_22(2), [1, 4])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            series_22(0)
        with self.assertRaises(ValueError):
            series_22(-5)

if __name__ == "__main__":
    unittest.main()
