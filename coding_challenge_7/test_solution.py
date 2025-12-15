import unittest
from solution import check_tax

class TestTaxCheck(unittest.TestCase):

    def test_above_limit(self):
        self.assertEqual(check_tax("Ravi", 500000), "Ravi must pay tax")

    def test_equal_limit(self):
        self.assertEqual(check_tax("Anu", 300000), "Anu does not need to pay tax")

    def test_below_limit(self):
        self.assertEqual(check_tax("Sita", 100000), "Sita does not need to pay tax")

    def test_negative_salary(self):
        self.assertEqual(check_tax("Test", -5000), "Test does not need to pay tax")


if __name__ == "__main__":
    unittest.main()
