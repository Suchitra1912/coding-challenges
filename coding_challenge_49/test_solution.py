import unittest

# Function to search element in array (for testing)
def search_element(arr, value):
    if value in arr:
        return arr.index(value)
    return -1

class TestSearchElement(unittest.TestCase):
    def test_found(self):
        self.assertEqual(search_element([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        self.assertEqual(search_element([1, 2, 3, 4, 5], 6), -1)

    def test_empty_array(self):
        self.assertEqual(search_element([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(search_element([10], 10), 0)

    def test_single_element_not_found(self):
        self.assertEqual(search_element([10], 5), -1)

if __name__ == "__main__":
    unittest.main()
