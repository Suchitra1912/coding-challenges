import unittest
from solution import generate_employee_report

class TestEmployeeReport(unittest.TestCase):

    def test_report_values(self):
        report = generate_employee_report(
            "John Doe", "E12345", 80000, 5000
        )

        self.assertEqual(report["Gross Monthly Salary"], 85000)
        self.assertEqual(report["Annual Gross Salary"], 1020000)
        self.assertEqual(report["Taxable Income"], 970000)
        self.assertEqual(report["Tax Payable"], 57720.0)
        self.assertEqual(report["Annual Net Salary"], 962280.0)

    def test_zero_salary(self):
        report = generate_employee_report("A", "E1", 0, 0)
        self.assertEqual(report["Annual Net Salary"], 0)

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            generate_employee_report("A", "E1", -1000, 2000)


if __name__ == "__main__":
    unittest.main()
