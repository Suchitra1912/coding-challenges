import unittest
from solution import factorial_pattern
from math import factorial

class TestFactorialPattern(unittest.TestCase):
    def test_first_row(self):
        self.assertEqual(factorial_pattern(1), [[1]])

    def test_three_rows(self):
        self.assertEqual(factorial_pattern(3), [[1], [1, 2], [1, 2, 6]])

    def test_five_rows(self):
        expected = [
            [1],
            [1, 2],
            [1, 2, 6],
            [1, 2, 6, 24],
            [1, 2, 6, 24, 120]
        ]
        self.assertEqual(factorial_pattern(5), expected)

if __name__ == "__main__":
    unittest.main()
