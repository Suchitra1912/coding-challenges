import unittest
from solution import find_maximum


class TestFindMaximum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_maximum([1, 3, 7, 2]), 7)

    def test_negative_numbers(self):
        self.assertEqual(find_maximum([-4, -1, -9]), -1)

    def test_single_element(self):
        self.assertEqual(find_maximum([5]), 5)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_maximum([])


if __name__ == "__main__":
    unittest.main()
