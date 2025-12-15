"""
Program: Basic Input and Salary Calculation
Author: Your Name
Date: YYYY-MM-DD
Description:
    Accepts employee details and calculates gross monthly and annual salary including bonus.
"""

def calculate_salary(basic_salary: float, allowances: float, bonus_percent: float) -> dict:
    """
    Calculate gross monthly and annual salary including bonus.

    Parameters:
        basic_salary (float): Basic monthly salary
        allowances (float): Special monthly allowances
        bonus_percent (float): Annual bonus as a percentage of gross monthly salary

    Returns:
        dict: Contains gross monthly salary, annual gross salary, and bonus
    """
    if basic_salary < 0 or allowances < 0 or bonus_percent < 0:
        raise ValueError("Salary, allowances, and bonus percentage must be non-negative.")

    gross_monthly = basic_salary + allowances
    bonus = (bonus_percent / 100) * (gross_monthly * 12)
    annual_gross = (gross_monthly * 12) + bonus

    return {
        "Gross Monthly Salary": gross_monthly,
        "Annual Bonus": bonus,
        "Annual Gross Salary": annual_gross
    }


def main():
    try:
        name = input("Enter Employee Name: ")
        emp_id = input("Enter Employee ID: ")
        basic_salary = float(input("Enter Basic Monthly Salary: "))
        allowances = float(input("Enter Special Allowances (Monthly): "))
        bonus_percent = float(input("Enter Bonus Percentage (%): "))

        salary_details = calculate_salary(basic_salary, allowances, bonus_percent)

        print("\nEmployee Details:")
        print(f"Name: {name}")
        print(f"EmpID: {emp_id}")
        print(f"Gross Monthly Salary: {salary_details['Gross Monthly Salary']}")
        print(f"Annual Bonus: {salary_details['Annual Bonus']}")
        print(f"Annual Gross Salary: {salary_details['Annual Gross Salary']}")

    except ValueError:
        print("Invalid input! Please enter numeric values for salaries and bonus percentage.")


if __name__ == "__main__":
    main()
