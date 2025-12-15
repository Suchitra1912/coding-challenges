"""
Program: Tax Calculator - New Tax Regime 2023
Author: Your Name
Date: YYYY-MM-DD
Description:
    Accepts employee salary details, calculates gross and taxable income,
    computes tax payable, applies deductions, and generates a salary report.
"""

def calculate_tax(income: float) -> float:
    """
    Calculate tax payable under the New Tax Regime (FY 2023-24)

    Parameters:
        income (float): Taxable annual income

    Returns:
        float: Tax payable
    """
    tax = 0
    # New Tax Regime slabs (FY 2023-24)
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 750000:
        tax = (250000 * 0.05) + (income - 500000) * 0.10
    elif income <= 1000000:
        tax = (250000 * 0.05) + (250000 * 0.10) + (income - 750000) * 0.15
    elif income <= 1250000:
        tax = (250000 * 0.05) + (250000 * 0.10) + (250000 * 0.15) + (income - 1000000) * 0.20
    elif income <= 1500000:
        tax = (250000 * 0.05) + (250000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (income - 1250000) * 0.25
    else:
        tax = (250000 * 0.05) + (250000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (250000 * 0.25) + (income - 1500000) * 0.30

    return tax

def generate_report(employee_name: str, monthly_salary: float) -> dict:
    """
    Generate salary and tax report for an employee.

    Parameters:
        employee_name (str): Employee name
        monthly_salary (float): Monthly salary

    Returns:
        dict: Report containing gross, taxable, tax payable, and net salary
    """
    if monthly_salary < 0:
        raise ValueError("Salary cannot be negative.")

    annual_gross = monthly_salary * 12
    # Standard deduction under New Tax Regime (2023)
    standard_deduction = 50000
    taxable_income = max(0, annual_gross - standard_deduction)

    tax_payable = calculate_tax(taxable_income)
    net_income = annual_gross - tax_payable

    report = {
        "Employee Name": employee_name,
        "Gross Salary": annual_gross,
        "Taxable Income": taxable_income,
        "Tax Payable": tax_payable,
        "Net Income": net_income
    }

    return report

def main():
    try:
        name = input("Enter employee name: ")
        salary = float(input("Enter monthly salary: "))

        report = generate_report(name, salary)

        print("\nSalary Report:")
        for key, value in report.items():
            if isinstance(value, float):
                print(f"{key}: ₹{value:.2f}")
            else:
                print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
