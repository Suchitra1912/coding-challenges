import unittest
from solution import star_pattern

class TestStarPattern(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(star_pattern(3), ['***', '***', '***'])
        self.assertEqual(star_pattern(5), ['*****']*5)

    def test_edge_case_one(self):
        self.assertEqual(star_pattern(1), ['*'])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            star_pattern(0)
        with self.assertRaises(ValueError):
            star_pattern(-3)
        with self.assertRaises(TypeError):
            star_pattern("5")
        with self.assertRaises(TypeError):
            star_pattern(2.5)

if __name__ == "__main__":
    unittest.main()
