import unittest
from unittest.mock import patch
from solution import store_elements

class TestStoreElements(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '20', '30'])
    def test_store_elements(self, mock_input):
        result = store_elements(3)
        self.assertEqual(result, [10, 20, 30])

    @patch('builtins.input', side_effect=['-5', '0', '5'])
    def test_store_elements_with_negative(self, mock_input):
        result = store_elements(3)
        self.assertEqual(result, [-5, 0, 5])

if __name__ == "__main__":
    unittest.main()
