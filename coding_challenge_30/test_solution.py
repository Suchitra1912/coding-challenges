import unittest
from solution import apply_promotional_discount

class TestPromotionalDiscount(unittest.TestCase):

    def test_no_promo_items(self):
        items = [{"code": "ITEM1", "description": "Item 1", "quantity": 2, "price": 100},
                 {"code": "ITEM2", "description": "Item 2", "quantity": 1, "price": 200}]
        self.assertEqual(apply_promotional_discount(items), 400.0)

    def test_with_promo_items(self):
        items = [{"code": "PROMO10", "description": "Promo Item", "quantity": 2, "price": 100},
                 {"code": "ITEM2", "description": "Item 2", "quantity": 1, "price": 200}]
        self.assertEqual(apply_promotional_discount(items), 380.0)

    def test_all_promo_items(self):
        items = [{"code": "PROMO10", "description": "Promo Item", "quantity": 3, "price": 50},
                 {"code": "PROMO10", "description": "Promo Item 2", "quantity": 2, "price": 100}]
        self.assertEqual(apply_promotional_discount(items), 315.0)

if __name__ == "__main__":
    unittest.main()
