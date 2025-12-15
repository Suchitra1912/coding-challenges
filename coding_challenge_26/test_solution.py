import unittest
from solution import compute_grand_total

class TestGrandTotal(unittest.TestCase):

    def test_single_item(self):
        items = [{"code": "A1", "desc": "Item1", "qty": 2, "price": 50}]
        self.assertEqual(compute_grand_total(items), 100)

    def test_multiple_items(self):
        items = [
            {"code": "A1", "desc": "Item1", "qty": 2, "price": 50},  # 100
            {"code": "B2", "desc": "Item2", "qty": 3, "price": 100}  # 300
        ]
        # Corrected expected value from 350 → 400
        self.assertEqual(compute_grand_total(items), 400)

    def test_empty_list(self):
        items = []
        self.assertEqual(compute_grand_total(items), 0)


if __name__ == "__main__":
    unittest.main()
