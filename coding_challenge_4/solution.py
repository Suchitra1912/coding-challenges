"""
Program: Swap Two Numbers
Author: Your Name
Date: YYYY-MM-DD
Description:
    Swaps the values of two numbers provided by the user.
"""

def swap_numbers(a: float, b: float) -> tuple[float, float]:
    """
    Swap two numbers.

    Parameters:
        a (float): First number
        b (float): Second number

    Returns:
        tuple: Swapped values (b, a)
    """
    return b, a


def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        a, b = swap_numbers(a, b)

        print(f"\nAfter swapping:")
        print(f"First number: {a}")
        print(f"Second number: {b}")

    except Exception:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
