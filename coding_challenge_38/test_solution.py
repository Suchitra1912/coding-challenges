import unittest
from solution import fibonacci_pattern

class TestFibonacciPattern38(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            fibonacci_pattern(4),
            [
                "1",
                "1 2",
                "3 5 8",
                "13 21 34 55"
            ]
        )

    def test_single_row(self):
        self.assertEqual(fibonacci_pattern(1), ["1"])

    def test_zero_rows(self):
        self.assertEqual(fibonacci_pattern(0), "Error")

    def test_negative_rows(self):
        self.assertEqual(fibonacci_pattern(-3), "Error")


if __name__ == "__main__":
    unittest.main()
