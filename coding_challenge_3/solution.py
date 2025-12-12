"""
Program: Discount Calculator
Author: Your Name
Date: YYYY-MM-DD
Description:
    Calculates the discount amount and final price based on total amount and discount rate.
"""

def calculate_discount(total_amount: float, discount_rate: float) -> float:
    """
    Calculate the discount amount.

    Parameters:
        total_amount (float): Total price before discount
        discount_rate (float): Discount rate in percent

    Returns:
        float: Discount amount rounded to 2 decimal places
    """
    if total_amount < 0 or discount_rate < 0:
        raise ValueError("Total amount and discount rate must be non-negative.")
    
    discount_amount = (total_amount * discount_rate) / 100
    return round(discount_amount, 2)


def main():
    try:
        total_amount = float(input("Enter the total amount: "))
        discount_rate = float(input("Enter the discount rate (%): "))

        discount = calculate_discount(total_amount, discount_rate)
        final_price = round(total_amount - discount, 2)

        print(f"\nDiscount Amount: {discount}")
        print(f"Final Price after Discount: {final_price}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
