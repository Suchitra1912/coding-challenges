"""
Program: Taxable Income Calculation
Author: Your Name
Date: YYYY-MM-DD
Description:
    Calculates taxable income after applying standard deduction from annual gross salary.
"""

STANDARD_DEDUCTION = 50000  # ₹50,000

def calculate_taxable_income(annual_gross_salary: float) -> dict:
    """
    Calculate taxable income after standard deduction.

    Parameters:
        annual_gross_salary (float): Annual gross salary

    Returns:
        dict: Contains gross salary, standard deduction, and taxable income
    """
    if annual_gross_salary < 0:
        raise ValueError("Annual gross salary must be non-negative.")

    taxable_income = max(annual_gross_salary - STANDARD_DEDUCTION, 0)

    return {
        "Gross Salary": annual_gross_salary,
        "Standard Deduction": STANDARD_DEDUCTION,
        "Taxable Income": taxable_income
    }


def main():
    try:
        annual_gross_salary = float(input("Enter Annual Gross Salary: "))

        result = calculate_taxable_income(annual_gross_salary)

        print("\nSalary Details:")
        print(f"Gross Salary: {result['Gross Salary']}")
        print(f"Standard Deduction: {result['Standard Deduction']}")
        print(f"Taxable Income: {result['Taxable Income']}")

    except ValueError:
        print("Invalid input! Please enter numeric values for salary.")


if __name__ == "__main__":
    main()
