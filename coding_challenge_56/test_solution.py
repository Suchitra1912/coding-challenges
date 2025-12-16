import unittest
from solution import sum_2d_array


class TestSum2DArray(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(sum_2d_array(matrix), 10)

    def test_single_row(self):
        matrix = [[5, 6, 7]]
        self.assertEqual(sum_2d_array(matrix), 18)

    def test_single_column(self):
        matrix = [[1], [2], [3]]
        self.assertEqual(sum_2d_array(matrix), 6)


if __name__ == "__main__":
    unittest.main()
