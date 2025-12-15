"""
Program: Check Even or Odd
Author: Your Name
Date: YYYY-MM-DD
Description:
    Checks whether a given number is even or odd.
"""

def check_even_odd(number: int) -> str:
    """
    Check if a number is even or odd.

    Parameters:
        number (int): Input number

    Returns:
        str: "Even" or "Odd"
    """
    return "Even" if number % 2 == 0 else "Odd"


def main():
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(f"The number is {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
