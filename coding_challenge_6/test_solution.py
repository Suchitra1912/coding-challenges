import unittest
from solution import check_even_odd

class TestEvenOdd(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(check_even_odd(10), "Even")
        self.assertEqual(check_even_odd(0), "Even")

    def test_odd_numbers(self):
        self.assertEqual(check_even_odd(7), "Odd")
        self.assertEqual(check_even_odd(-5), "Odd")

    def test_negative_even(self):
        self.assertEqual(check_even_odd(-8), "Even")


if __name__ == "__main__":
    unittest.main()
