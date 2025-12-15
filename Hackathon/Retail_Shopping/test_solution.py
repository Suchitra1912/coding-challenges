import unittest
from solution import add_item, calculate_total, apply_discount, generate_invoice, items

class TestRetailShopping(unittest.TestCase):

    def setUp(self):
        # Clear the items dictionary before each test
        items.clear()

    def test_add_and_total(self):
        add_item("Apple", 100, 2)
        add_item("Banana", 50, 3)
        self.assertEqual(calculate_total(), 100*2 + 50*3)

    def test_discount(self):
        add_item("Apple", 100, 2)
        total = calculate_total()
        discounted = apply_discount(total, 10)  # 10% discount
        self.assertEqual(discounted, total * 0.9)

    def test_invalid_item(self):
        with self.assertRaises(ValueError):
            add_item("Orange", -10, 2)
        with self.assertRaises(ValueError):
            add_item("Orange", 10, 0)

    def test_invoice(self):
        add_item("Apple", 100, 2)
        invoice = generate_invoice(discount=10)
        self.assertEqual(invoice["Total Before Discount"], 200)
        self.assertEqual(invoice["Total After Discount"], 180)

if __name__ == "__main__":
    unittest.main()
