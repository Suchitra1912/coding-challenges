"""
Program: Employee Tax Report Generation
Description:
    Generates a detailed employee tax report.
"""

def calculate_tax(taxable_income: float) -> float:
    if taxable_income <= 700000:
        return 0.0

    tax = 0.0
    remaining = taxable_income - 300000

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
        slab = min(remaining, limit)
        tax += slab * rate
        remaining -= slab

    tax += tax * 0.04
    return round(tax, 2)


def generate_employee_report(name, emp_id, basic_salary, special_allowance):
    if basic_salary < 0 or special_allowance < 0:
        raise ValueError("Salary cannot be negative")

    gross_monthly = basic_salary + special_allowance
    annual_gross = gross_monthly * 12
    taxable_income = annual_gross - 50000
    tax = calculate_tax(taxable_income)
    net_salary = annual_gross - tax

    return {
        "Name": name,
        "EmpID": emp_id,
        "Gross Monthly Salary": gross_monthly,
        "Annual Gross Salary": annual_gross,
        "Taxable Income": taxable_income,
        "Tax Payable": tax,
        "Annual Net Salary": net_salary
    }


def main():
    name = input("Enter Name: ")
    emp_id = input("Enter EmpID: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Special Allowance: "))

    report = generate_employee_report(name, emp_id, basic, allowance)

    print("\nEmployee Tax Report")
    print("-" * 40)
    for k, v in report.items():
        if isinstance(v, float):
            print(f"{k:<25} ₹{v:,.2f}")
        else:
            print(f"{k:<25} {v}")


if __name__ == "__main__":
    main()
