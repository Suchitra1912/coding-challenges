import unittest
from solution import element_exists


class TestElementExists(unittest.TestCase):

    def test_element_found(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertTrue(element_exists(matrix, 5))

    def test_element_not_found(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(element_exists(matrix, 9))

    def test_single_element_matrix(self):
        matrix = [[10]]
        self.assertTrue(element_exists(matrix, 10))


if __name__ == "__main__":
    unittest.main()
