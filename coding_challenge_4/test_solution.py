import unittest
from solution import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_swap_positive_numbers(self):
        self.assertEqual(swap_numbers(5, 10), (10, 5))
        self.assertEqual(swap_numbers(100, 200), (200, 100))

    def test_swap_negative_numbers(self):
        self.assertEqual(swap_numbers(-5, -10), (-10, -5))
        self.assertEqual(swap_numbers(-100, 50), (50, -100))

    def test_swap_zero(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))
        self.assertEqual(swap_numbers(0, 10), (10, 0))
        self.assertEqual(swap_numbers(-10, 0), (0, -10))

    def test_swap_floats(self):
        self.assertEqual(swap_numbers(1.5, 2.5), (2.5, 1.5))
        self.assertEqual(swap_numbers(-1.2, 3.4), (3.4, -1.2))

if __name__ == "__main__":
    unittest.main()
