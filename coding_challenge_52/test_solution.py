import unittest

# Function to reverse an array (for testing)
def reverse_array(arr):
    return arr[::-1]

class TestReverseArray(unittest.TestCase):
    def test_normal_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_single_element(self):
        self.assertEqual(reverse_array([10]), [10])

    def test_empty_array(self):
        self.assertEqual(reverse_array([]), [])

    def test_negative_elements(self):
        self.assertEqual(reverse_array([-1, -2, -3]), [-3, -2, -1])

if __name__ == "__main__":
    unittest.main()
