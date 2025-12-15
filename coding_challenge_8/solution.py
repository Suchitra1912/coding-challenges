"""
Program: Largest of Three Numbers
Author: Your Name
Date: YYYY-MM-DD
Description:
    Finds the largest among three numbers.
"""

def largest_of_three(a: int, b: int, c: int) -> int:
    """
    Find the largest of three numbers.

    Returns:
        int: Largest number
    """
    return max(a, b, c)


def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))

        print(f"Largest number is: {largest_of_three(a, b, c)}")
    except ValueError:
        print("Invalid input! Please enter integers.")


if __name__ == "__main__":
    main()
