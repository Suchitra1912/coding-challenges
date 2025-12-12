"""
Program: Simple Interest Calculator
Author: Your Name
Date: YYYY-MM-DD
Description:
    Calculates the Simple Interest (SI) based on principal, rate, and time.
    SI = (P * R * T) / 100
"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate the simple interest.

    Parameters:
        principal (float): The principal amount (P)
        rate (float): Annual interest rate in percent (R)
        time (float): Time in years (T)

    Returns:
        float: Simple interest rounded to 2 decimal places
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")
    
    simple_interest = (principal * rate * time) / 100
    return round(simple_interest, 2)


def main():
    # Input from the user
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest (% per year): "))
        time = float(input("Enter the time (in years): "))
        
        si = calculate_simple_interest(principal, rate, time)
        total_amount = round(principal + si, 2)

        print(f"\nSimple Interest: {si}")
        print(f"Total Amount (Principal + Interest): {total_amount}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
