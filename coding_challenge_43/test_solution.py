import unittest
from solution import separate_whole_fraction

class TestSeparate(unittest.TestCase):
    def test_example(self):
        self.assertEqual(separate_whole_fraction(123.456), (123, 0.456))

if __name__ == "__main__":
    unittest.main()
