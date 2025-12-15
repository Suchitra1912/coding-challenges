import unittest
from solution import validate_and_calculate

class TestInputValidation(unittest.TestCase):

    def test_valid_inputs(self):
        result = validate_and_calculate("John", "EMP123", 50000, 10000, 10)
        self.assertEqual(result["Name"], "John")
        self.assertEqual(result["EmpID"], "EMP123")
        self.assertEqual(result["Basic Salary"], 50000)
        self.assertEqual(result["Special Allowances"], 10000)
        self.assertEqual(result["Bonus Percentage"], 10)
        self.assertEqual(result["Gross Monthly Salary"], 60000)
        self.assertEqual(result["Annual Gross Salary"], 720000)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            validate_and_calculate("", "EMP123", 50000, 10000, 10)

    def test_invalid_empid(self):
        with self.assertRaises(ValueError):
            validate_and_calculate("John", "EMP!", 50000, 10000, 10)

    def test_invalid_basic_salary(self):
        with self.assertRaises(ValueError):
            validate_and_calculate("John", "EMP123", -50000, 10000, 10)

    def test_invalid_allowances(self):
        with self.assertRaises(ValueError):
            validate_and_calculate("John", "EMP123", 50000, -10000, 10)

    def test_invalid_bonus_percentage(self):
        with self.assertRaises(ValueError):
            validate_and_calculate("John", "EMP123", 50000, 10000, 150)

if __name__ == "__main__":
    unittest.main()
