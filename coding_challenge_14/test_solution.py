import unittest
from solution import calculate_net_salary

class TestNetSalaryCalculation(unittest.TestCase):

    def test_net_salary_normal(self):
        result = calculate_net_salary(800000)
        self.assertEqual(result["Total Tax Payable"], 36400.0)
        self.assertEqual(result["Annual Net Salary"], 763600.0)

    def test_no_tax_salary(self):
        result = calculate_net_salary(600000)
        self.assertEqual(result["Total Tax Payable"], 0.0)
        self.assertEqual(result["Annual Net Salary"], 600000.0)

    def test_zero_salary(self):
        result = calculate_net_salary(0)
        self.assertEqual(result["Annual Net Salary"], 0)

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            calculate_net_salary(-10000)


if __name__ == "__main__":
    unittest.main()
