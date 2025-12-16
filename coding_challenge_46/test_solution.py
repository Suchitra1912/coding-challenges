import unittest

# Function to calculate sum (for testing purpose)
def array_sum(arr):
    return sum(arr)

class TestArraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(array_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(array_sum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(array_sum([1, -2, 3]), 2)

    def test_empty_array(self):
        self.assertEqual(array_sum([]), 0)

if __name__ == "__main__":
    unittest.main()
