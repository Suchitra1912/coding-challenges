import unittest
from solution import number_increasing_pattern

class TestNumberIncreasingPattern37(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            number_increasing_pattern(4),
            ["1", "12", "123", "1234"]
        )

    def test_single_row(self):
        self.assertEqual(number_increasing_pattern(1), ["1"])

    def test_zero_rows(self):
        self.assertEqual(number_increasing_pattern(0), "Error")

    def test_negative_rows(self):
        self.assertEqual(number_increasing_pattern(-5), "Error")


if __name__ == "__main__":
    unittest.main()
