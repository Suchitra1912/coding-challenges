# test_solution.py
import unittest
from solution import challenge_function

class TestChallenge(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(challenge_function(5), 25)

    def test_edge_case(self):
        self.assertEqual(challenge_function(0), 0)

    def test_invalid_case(self):
        with self.assertRaises(ValueError):
            challenge_function(-1)

if __name__ == "__main__":
    unittest.main()
