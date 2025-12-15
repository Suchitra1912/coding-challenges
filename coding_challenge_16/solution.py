import re

MAX_SALARY = 10_000_000  # Maximum salary limit: ₹1,00,00,000
MAX_NAME_LENGTH = 50     # Maximum length for name
MAX_BONUS_PERCENTAGE = 100  # Maximum bonus percentage

# Validation Functions

def validate_name(name: str) -> str:
    """Validate that the name is non-empty, alphabetic, and up to 50 characters."""
    if not name or not name.isalpha() or len(name) > MAX_NAME_LENGTH:
        raise ValueError("Invalid Name: Must be non-empty, alphabets only, and up to 50 characters.")
    return name

def validate_empid(emp_id: str) -> str:
    """Validate that the EmpID is alphanumeric and 5–10 characters long."""
    if not re.match(r"^[A-Za-z0-9]{5,10}$", emp_id):
        raise ValueError("Invalid EmpID: Must be alphanumeric and 5–10 characters long.")
    return emp_id

def validate_basic_salary(basic: float) -> float:
    """Validate that the basic salary is positive and not exceeding the maximum limit."""
    if basic <= 0 or basic > MAX_SALARY:
        raise ValueError("Invalid Basic Salary: Must be positive and not exceed ₹1,00,00,000.")
    return basic

def validate_allowances(allowances: float) -> float:
    """Validate that the allowances are non-negative and not exceeding the maximum limit."""
    if allowances < 0 or allowances > MAX_SALARY:
        raise ValueError("Invalid Special Allowances: Must be non-negative and not exceed ₹1,00,00,000.")
    return allowances

def validate_bonus_percentage(bonus: float) -> float:
    """Validate that the bonus percentage is between 0 and 100."""
    if bonus < 0 or bonus > MAX_BONUS_PERCENTAGE:
        raise ValueError("Invalid Bonus Percentage: Must be between 0 and 100.")
    return bonus

# Validation and Calculation Wrapper

def validate_and_calculate(
    name: str,
    emp_id: str,
    basic_salary: float,
    special_allowances: float,
    bonus_percentage: float
) -> dict:
    """Validate all inputs and compute derived salary details."""
    name = validate_name(name)
    emp_id = validate_empid(emp_id)
    basic_salary = validate_basic_salary(basic_salary)
    special_allowances = validate_allowances(special_allowances)
    bonus_percentage = validate_bonus_percentage(bonus_percentage)

    gross_monthly_salary = basic_salary + special_allowances
    if gross_monthly_salary <= 0:
        raise ValueError("Gross Monthly Salary must be greater than zero.")

    annual_gross_salary = gross_monthly_salary * 12
    if annual_gross_salary > 50_000_000:  # Realistic upper bound
        raise ValueError("Annual Gross Salary exceeds realistic limits.")

    return {
        "Name": name,
        "EmpID": emp_id,
        "Basic Salary": basic_salary,
        "Special Allowances": special_allowances,
        "Bonus Percentage": bonus_percentage,
        "Gross Monthly Salary": gross_monthly_salary,
        "Annual Gross Salary": annual_gross_salary
    }
