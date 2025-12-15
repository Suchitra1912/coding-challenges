"""
Program: Tax Eligibility Check
Author: Your Name
Date: YYYY-MM-DD
Description:
    Checks whether a person must pay tax based on salary.
"""

TAX_LIMIT = 300000

def check_tax(name: str, salary: int) -> str:
    """
    Check tax eligibility.

    Parameters:
        name (str): Person name
        salary (int): Annual salary

    Returns:
        str: Tax status message
    """
    if salary > TAX_LIMIT:
        return f"{name} must pay tax"
    return f"{name} does not need to pay tax"


def main():
    try:
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        print(check_tax(name, salary))
    except ValueError:
        print("Invalid input! Salary must be a number.")


if __name__ == "__main__":
    main()
