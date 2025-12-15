import unittest
from solution import generate_report, calculate_tax

class TestTaxCalculator(unittest.TestCase):

    def test_tax_calculation(self):
        # Tax-free income
        self.assertEqual(calculate_tax(200000), 0)
        # Income in 5% slab
        self.assertEqual(calculate_tax(400000), 7500.0)      # 5% of 150,000
        # Income in 10% slab
        self.assertEqual(calculate_tax(600000), 22500.0)     # 5% of 250,000 + 10% of 100,000
        # Income in 15% slab
        self.assertEqual(calculate_tax(800000), 45000.0)     # 5% +10% +15%
        # Income in 20% slab
        self.assertEqual(calculate_tax(1100000), 95000.0)    # 5% +10% +15% +20%
        # Income in 25% slab
        self.assertEqual(calculate_tax(1300000), 140000.0)   # 5% +10% +15% +20% +25%
        # Income in 30% slab
        self.assertEqual(calculate_tax(1600000), 215000.0)   # 5% +10% +15% +20% +25% +30%

    def test_generate_report(self):
        # Monthly salary = 50,000 → Annual = 600,000 → Taxable = 550,000
        report = generate_report("Alice", 50000)
        self.assertAlmostEqual(report["Gross Salary"], 600000)
        self.assertAlmostEqual(report["Taxable Income"], 550000)
        self.assertAlmostEqual(report["Tax Payable"], 17500.0)  # 5% of 250,000 + 10% of 50,000
        self.assertAlmostEqual(report["Net Income"], 582500.0)

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            generate_report("Bob", -10000)

    def test_zero_salary(self):
        report = generate_report("Charlie", 0)
        self.assertEqual(report["Gross Salary"], 0)
        self.assertEqual(report["Taxable Income"], 0)
        self.assertEqual(report["Tax Payable"], 0)
        self.assertEqual(report["Net Income"], 0)

if __name__ == "__main__":
    unittest.main()
