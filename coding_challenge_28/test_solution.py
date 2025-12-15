import unittest
from solution import apply_membership_discount

class TestMembershipDiscount(unittest.TestCase):

    def test_member_discount(self):
        self.assertEqual(apply_membership_discount(1000, 'y'), 980.0)
        self.assertEqual(apply_membership_discount(5000, 'Y'), 4900.0)

    def test_non_member_no_discount(self):
        self.assertEqual(apply_membership_discount(1000, 'n'), 1000.0)
        self.assertEqual(apply_membership_discount(5000, 'N'), 5000.0)

    def test_invalid_input_string(self):
        self.assertEqual(apply_membership_discount(1000, 'abc'), 1000.0)

if __name__ == "__main__":
    unittest.main()
