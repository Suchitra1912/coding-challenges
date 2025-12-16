import unittest
from solution import reverse_number

class TestReverseNumber(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reverse_number(12345), 54321)

if __name__ == "__main__":
    unittest.main()
