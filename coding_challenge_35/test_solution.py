import unittest
from solution import print_star_pattern

class TestStarPattern(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(print_star_pattern(4), ["*", "**", "***", "****"])

    def test_single_row(self):
        self.assertEqual(print_star_pattern(1), ["*"])

    def test_zero_input(self):
        self.assertEqual(print_star_pattern(0), "Error")

    def test_negative_input(self):
        self.assertEqual(print_star_pattern(-3), "Error")


if __name__ == "__main__":
    unittest.main()
