# Test cases for Coding Challenge 34: Printing Number Pattern (N Rows)

import unittest
from solution import print_number_pattern

class TestNumberPattern34(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(print_number_pattern(3), ["123", "123", "123"])

    def test_five_rows(self):
        self.assertEqual(
            print_number_pattern(5),
            ["12345", "12345", "12345", "12345", "12345"]
        )

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            print_number_pattern(0)
        with self.assertRaises(ValueError):
            print_number_pattern(-1)


if __name__ == "__main__":
    unittest.main()
