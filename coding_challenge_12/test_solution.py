import unittest
from solution import calculate_taxable_income, STANDARD_DEDUCTION

class TestTaxableIncomeCalculation(unittest.TestCase):

    def test_taxable_income(self):
        result = calculate_taxable_income(600000)
        self.assertEqual(result["Gross Salary"], 600000)
        self.assertEqual(result["Standard Deduction"], STANDARD_DEDUCTION)
        self.assertEqual(result["Taxable Income"], 550000)

    def test_zero_salary(self):
        result = calculate_taxable_income(0)
        self.assertEqual(result["Gross Salary"], 0)
        self.assertEqual(result["Standard Deduction"], STANDARD_DEDUCTION)
        self.assertEqual(result["Taxable Income"], 0)

    def test_salary_equal_to_deduction(self):
        result = calculate_taxable_income(50000)
        self.assertEqual(result["Taxable Income"], 0)

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            calculate_taxable_income(-10000)

if __name__ == "__main__":
    unittest.main()
