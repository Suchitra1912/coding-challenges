import unittest
from solution import series_23

class TestSeries23(unittest.TestCase):
    def test_series_generation(self):
        self.assertEqual(series_23(5), [1, 5, 9, 13, 21])
        self.assertEqual(series_23(1), [1])
        self.assertEqual(series_23(2), [1, 5])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            series_23(0)
        with self.assertRaises(ValueError):
            series_23(-5)

if __name__ == "__main__":
    unittest.main()
