import unittest
from solution import calculate_final_amount

class TestPaymentMode(unittest.TestCase):

    def test_cash_payment(self):
        total, surcharge = calculate_final_amount(1000, "Cash")
        self.assertEqual(total, 1000)
        self.assertEqual(surcharge, 0.0)

    def test_credit_card_payment(self):
        total, surcharge = calculate_final_amount(1000, "Credit Card")
        self.assertAlmostEqual(total, 1020.0)
        self.assertAlmostEqual(surcharge, 20.0)

    def test_case_insensitive(self):
        total, surcharge = calculate_final_amount(500, "credit card")
        self.assertAlmostEqual(total, 510.0)
        self.assertAlmostEqual(surcharge, 10.0)


if __name__ == "__main__":
    unittest.main()
