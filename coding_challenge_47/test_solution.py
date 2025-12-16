import unittest

# Function to find minimum value (for testing)
def find_min(arr):
    if not arr:
        return None
    return min(arr)

class TestFindMin(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_min([5, 2, 9, 1, 7]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_min([-5, -2, -9, -1]), -9)

    def test_mixed_numbers(self):
        self.assertEqual(find_min([5, -2, 9, -1]), -2)

    def test_single_element(self):
        self.assertEqual(find_min([42]), 42)

    def test_empty_array(self):
        self.assertIsNone(find_min([]))

if __name__ == "__main__":
    unittest.main()
