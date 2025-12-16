import unittest
from solution import multiply_matrices


class TestMatrixMultiplication(unittest.TestCase):

    def test_valid_multiplication(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = multiply_matrices(A, B)
        self.assertEqual(result, [[19, 22], [43, 50]])

    def test_rectangular_matrices(self):
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        result = multiply_matrices(A, B)
        self.assertEqual(result, [[58, 64], [139, 154]])

    def test_invalid_multiplication(self):
        A = [[1, 2]]
        B = [[3, 4]]
        with self.assertRaises(ValueError):
            multiply_matrices(A, B)


if __name__ == "__main__":
    unittest.main()
