import unittest
from solution import sort_array


class TestSortArray(unittest.TestCase):

    def test_ascending_order(self):
        self.assertEqual(sort_array([3, 1, 4, 2], "asc"), [1, 2, 3, 4])

    def test_descending_order(self):
        self.assertEqual(sort_array([3, 1, 4, 2], "desc"), [4, 3, 2, 1])

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            sort_array([1, 2, 3], "invalid")


if __name__ == "__main__":
    unittest.main()
