import unittest
from solution import calculate_sales

class TestFarmerSales(unittest.TestCase):

    def test_calculate_sales(self):
        """
        This test checks if the overall sales and chemical-free sales
        are correctly calculated based on the given problem statement.
        """

        # Since calculate_sales() prints values, we can capture them using a context manager
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        calculate_sales()

        sys.stdout = sys.__stdout__  # Reset redirect.

        output = captured_output.getvalue()

        # Expected sales values based on manual calculation
        expected_total_sales = 14972800  # Rs
        expected_output_lines = [
            f"Overall Sales from 80 acres: Rs {expected_total_sales:,}",
            f"Sales from Chemical-Free Farming at 11 months: Rs {expected_total_sales:,}"
        ]

        # Check that both expected lines are in output
        for line in expected_output_lines:
            self.assertIn(line, output)

if __name__ == "__main__":
    unittest.main()
