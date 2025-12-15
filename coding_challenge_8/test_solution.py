import unittest
from solution import largest_of_three

class TestLargestOfThree(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(largest_of_three(10, 20, 5), 20)

    def test_negative_numbers(self):
        self.assertEqual(largest_of_three(-1, -5, -3), -1)

    def test_equal_numbers(self):
        self.assertEqual(largest_of_three(5, 5, 5), 5)

    def test_mixed_numbers(self):
        self.assertEqual(largest_of_three(-10, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
