import unittest
from solution import calculate_class

class TestStudentReportCard(unittest.TestCase):

    def test_first_class(self):
        self.assertEqual(calculate_class([70, 65, 80]), (215, 71.66666666666667, "1st Class"))

    def test_second_class(self):
        self.assertEqual(calculate_class([50, 55, 60]), (165, 55.0, "2nd Class"))

    def test_pass_class(self):
        self.assertEqual(calculate_class([35, 40, 50]), (125, 41.666666666666664, "Pass Class"))

    def test_fail(self):
        self.assertEqual(calculate_class([20, 30, 40]), (90, 30.0, "Fail"))

    def test_invalid_scores_length(self):
        with self.assertRaises(ValueError):
            calculate_class([50, 60])  # Less than 3 scores

    def test_exact_boundary(self):
        self.assertEqual(calculate_class([60, 60, 60]), (180, 60.0, "1st Class"))
        self.assertEqual(calculate_class([50, 50, 50]), (150, 50.0, "2nd Class"))
        self.assertEqual(calculate_class([35, 35, 35]), (105, 35.0, "Pass Class"))

if __name__ == "__main__":
    unittest.main()
