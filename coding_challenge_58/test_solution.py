import unittest
from solution import create_matrix, transpose_matrix


class TestMatrixOperations(unittest.TestCase):

    def test_matrix_creation(self):
        result = create_matrix(2, 3, [1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6]])

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, [[1, 4], [2, 5], [3, 6]])

    def test_square_matrix_transpose(self):
        matrix = [[1, 2], [3, 4]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, [[1, 3], [2, 4]])


if __name__ == "__main__":
    unittest.main()
