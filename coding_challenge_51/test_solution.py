import unittest
from solution import store_elements


class TestStoreElements(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(store_elements(3, [1, 2, 3]), [1, 2, 3])

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            store_elements(0, [])

    def test_mismatch_elements(self):
        with self.assertRaises(ValueError):
            store_elements(2, [1])


if __name__ == "__main__":
    unittest.main()
