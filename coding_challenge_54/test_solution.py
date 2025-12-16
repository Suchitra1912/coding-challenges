import unittest
from solution import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_element_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_element_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)

    def test_first_element(self):
        self.assertEqual(binary_search([2, 4, 6, 8], 2), 0)

    def test_last_element(self):
        self.assertEqual(binary_search([2, 4, 6, 8], 8), 3)


if __name__ == "__main__":
    unittest.main()
