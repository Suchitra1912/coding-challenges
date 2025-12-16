import unittest
from solution import print_number_pattern

class TestNumberPattern(unittest.TestCase):

    def test_small_input(self):
        # Normal case
        self.assertEqual(print_number_pattern(3), ["111", "222", "333"])

    def test_larger_input(self):
        # Larger valid input
        self.assertEqual(
            print_number_pattern(5),
            ["11111", "22222", "33333", "44444", "55555"]
        )

    def test_invalid_input(self):
        # Edge cases
        with self.assertRaises(ValueError):
            print_number_pattern(0)
        with self.assertRaises(ValueError):
            print_number_pattern(-2)


if __name__ == "__main__":
    unittest.main()
