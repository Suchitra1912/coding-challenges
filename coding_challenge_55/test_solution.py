import unittest
from solution import create_2d_array


class Test2DArray(unittest.TestCase):

    def test_matrix_creation(self):
        result = create_2d_array(2, 2, [1, 2, 3, 4])
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_single_row(self):
        result = create_2d_array(1, 3, [5, 6, 7])
        self.assertEqual(result, [[5, 6, 7]])


if __name__ == "__main__":
    unittest.main()
