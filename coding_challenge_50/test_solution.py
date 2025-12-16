import unittest
from solution import count_odd_even


class TestOddEvenCount(unittest.TestCase):

    def test_mixed_numbers(self):
        self.assertEqual(count_odd_even([1, 2, 3, 4, 5]), (3, 2))

    def test_all_even(self):
        self.assertEqual(count_odd_even([2, 4, 6]), (0, 3))

    def test_all_odd(self):
        self.assertEqual(count_odd_even([1, 3, 5]), (3, 0))

    def test_single_element(self):
        self.assertEqual(count_odd_even([10]), (0, 1))


if __name__ == "__main__":
    unittest.main()
