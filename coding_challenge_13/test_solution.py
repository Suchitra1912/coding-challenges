import unittest
from solution import calculate_tax


class TestTaxCalculation(unittest.TestCase):

    def test_no_tax_due_to_rebate(self):
        result = calculate_tax(700000)
        self.assertEqual(result["total_tax"], 0)

    def test_tax_above_rebate_limit(self):
        result = calculate_tax(800000)
        self.assertGreater(result["total_tax"], 0)

    def test_high_income_tax(self):
        result = calculate_tax(2000000)
        self.assertGreater(result["total_tax"], 0)

    def test_cess_calculation(self):
        result = calculate_tax(1000000)
        self.assertAlmostEqual(result["cess"], result["tax_after_rebate"] * 0.04)


if __name__ == "__main__":
    unittest.main()
