import unittest
from solution import calculate_salary

class TestSalaryCalculation(unittest.TestCase):

    def test_basic_calculation(self):
        result = calculate_salary(50000, 10000, 10)
        self.assertAlmostEqual(result["Gross Monthly Salary"], 60000)
        self.assertAlmostEqual(result["Annual Bonus"], 72000)  # 10% of (60000*12)
        self.assertAlmostEqual(result["Annual Gross Salary"], 792000)  # 60000*12 + 72000

    def test_zero_bonus(self):
        result = calculate_salary(40000, 5000, 0)
        self.assertEqual(result["Gross Monthly Salary"], 45000)
        self.assertEqual(result["Annual Bonus"], 0)
        self.assertEqual(result["Annual Gross Salary"], 540000)

    def test_zero_allowances(self):
        result = calculate_salary(50000, 0, 5)
        self.assertEqual(result["Gross Monthly Salary"], 50000)
        self.assertEqual(result["Annual Bonus"], 30000)  # 5% of (50000*12)
        self.assertEqual(result["Annual Gross Salary"], 630000)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_salary(-50000, 10000, 10)
        with self.assertRaises(ValueError):
            calculate_salary(50000, -10000, 10)
        with self.assertRaises(ValueError):
            calculate_salary(50000, 10000, -5)

if __name__ == "__main__":
    unittest.main()
