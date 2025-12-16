import unittest
from solution import number_to_words

class TestNumberToWords(unittest.TestCase):
    def test_example(self):
        self.assertEqual(number_to_words(270176), "Two Seven Zero One Seven Six")

if __name__ == "__main__":
    unittest.main()
