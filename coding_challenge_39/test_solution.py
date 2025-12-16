import unittest
from solution import square_pattern

class TestSquarePattern39(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            square_pattern(4),
            [
                "1",
                "-4 9",
                "-16 25 -36",
                "49 -64 81 -100"
            ]
        )

    def test_single_row(self):
        self.assertEqual(square_pattern(1), ["1"])

    def test_zero_rows(self):
        self.assertEqual(square_pattern(0), "Error")

    def test_negative_rows(self):
        self.assertEqual(square_pattern(-2), "Error")


if __name__ == "__main__":
    unittest.main()
