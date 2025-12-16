import unittest

# Import functions/constants from the main program
from healwell_hospital import (
    calculate_discounts,
    GST_RATE
)


class TestHealWellHospitalBilling(unittest.TestCase):

    # ---------- Discount Tests ----------

    def test_no_discount(self):
        """No discount for age < 60 and subtotal <= 5000"""
        age = 35
        subtotal = 2000
        discount = calculate_discounts(age, subtotal)
        self.assertEqual(discount, 0)

    def test_senior_citizen_discount(self):
        """10% discount for senior citizens"""
        age = 65
        subtotal = 4000
        discount = calculate_discounts(age, subtotal)
        self.assertEqual(discount, 400)  # 10% of 4000

    def test_high_bill_discount_only(self):
        """5% discount if subtotal > 5000"""
        age = 40
        subtotal = 6000
        discount = calculate_discounts(age, subtotal)
        self.assertEqual(discount, 300)  # 5% of 6000

    def test_both_discounts_applied(self):
        """
        Senior discount first (10%),
        then high-bill discount (5% on reduced subtotal)
        """
        age = 65
        subtotal = 6000

        # Senior discount = 600
        # Remaining = 5400
        # High bill discount = 270
        expected_discount = 870

        discount = calculate_discounts(age, subtotal)
        self.assertEqual(discount, expected_discount)

    # ---------- GST Calculation Test ----------

    def test_gst_calculation(self):
        """GST should be 18% of discounted amount"""
        discounted_total = 2000
        gst = discounted_total * GST_RATE
        self.assertEqual(gst, 360)


if __name__ == "__main__":
    unittest.main()
