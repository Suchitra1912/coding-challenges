"""
Program: Net Salary Calculation
Author: Your Name
Date: YYYY-MM-DD
Description:
    Calculates annual net salary after tax deductions
    using New Tax Regime (2023).
"""

def calculate_tax(taxable_income: float) -> float:
    """
    Calculate tax payable based on New Tax Regime (2023)
    including Section 87A rebate and 4% cess.
    """
    if taxable_income <= 700000:
        return 0.0

    tax = 0.0
    remaining = taxable_income - 300000  # First 3L exempt

    slabs = [
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float("inf"), 0.30)
    ]

    for limit, rate in slabs:
        if remaining <= 0:
            break
        slab_amount = min(remaining, limit)
        tax += slab_amount * rate
        remaining -= slab_amount

    # Add 4% cess
    tax += tax * 0.04
    return round(tax, 2)


def calculate_net_salary(annual_gross_salary: float) -> dict:
    """
    Calculate annual net salary after tax deduction.
    """
    if annual_gross_salary < 0:
        raise ValueError("Salary cannot be negative")

    tax = calculate_tax(annual_gross_salary)
    net_salary = annual_gross_salary - tax

    return {
        "Annual Gross Salary": annual_gross_salary,
        "Total Tax Payable": tax,
        "Annual Net Salary": net_salary
    }


def main():
    try:
        salary = float(input("Enter Annual Gross Salary: "))
        result = calculate_net_salary(salary)

        print("\nSalary Details")
        print(f"Annual Gross Salary: {result['Annual Gross Salary']}")
        print(f"Total Tax Payable: {result['Total Tax Payable']}")
        print(f"Annual Net Salary: {result['Annual Net Salary']}")

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()
