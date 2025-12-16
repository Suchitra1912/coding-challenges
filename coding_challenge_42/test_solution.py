import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_example(self):
        self.assertEqual(generate_series(6), [1, -5, 9, -13, 17, -21])

if __name__ == "__main__":
    unittest.main()
