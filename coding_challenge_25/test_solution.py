import unittest
from solution import calculate_item_total

class TestItemTotal(unittest.TestCase):

    def test_positive_values(self):
        result = calculate_item_total("A001", "Pen", 10, 15.0)
        self.assertEqual(result["Total"], 150.0)

    def test_zero_quantity(self):
        result = calculate_item_total("A002", "Notebook", 0, 50.0)
        self.assertEqual(result["Total"], 0.0)

    def test_zero_price(self):
        result = calculate_item_total("A003", "Eraser", 5, 0.0)
        self.assertEqual(result["Total"], 0.0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_item_total("A004", "Marker", -5, 20.0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_item_total("A005", "Ruler", 5, -10.0)

if __name__ == "__main__":
    unittest.main()
