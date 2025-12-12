import unittest
from solution import calculate_simple_interest

class TestSimpleInterest(unittest.TestCase):
    
    def test_positive_values(self):
        self.assertEqual(calculate_simple_interest(1000, 5, 3), 150.00)
        self.assertEqual(calculate_simple_interest(5000, 7.5, 2), 750.00)

    def test_zero_values(self):
        self.assertEqual(calculate_simple_interest(0, 5, 3), 0.00)
        self.assertEqual(calculate_simple_interest(1000, 0, 3), 0.00)
        self.assertEqual(calculate_simple_interest(1000, 5, 0), 0.00)

    def test_edge_cases(self):
        self.assertEqual(calculate_simple_interest(1e6, 0.01, 1), 100.00)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(-1000, 5, 3)
        with self.assertRaises(ValueError):
            calculate_simple_interest(1000, -5, 3)
        with self.assertRaises(ValueError):
            calculate_simple_interest(1000, 5, -3)

if __name__ == "__main__":
    unittest.main()
