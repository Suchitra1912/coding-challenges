"""
Coding Challenge 29: Tax Calculation Based on Purchase Amount
Objective: Apply tiered tax rates based on grand total.
"""

def calculate_tax_on_purchase(grand_total: float) -> tuple[float, float]:
    """
    Calculate tax and grand total including tax.

    Parameters:
        grand_total (float): Total amount before tax

    Returns:
        tuple: (tax_amount, total_with_tax)
    """
    if grand_total < 5000:
        tax_rate = 0.05
    elif 5000 <= grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = round(grand_total * tax_rate, 2)
    total_with_tax = round(grand_total + tax_amount, 2)
    return tax_amount, total_with_tax


def main():
    try:
        grand_total = float(input("Enter the grand total: ₹"))
        tax_amount, total_with_tax = calculate_tax_on_purchase(grand_total)
        print(f"Tax Amount: ₹{tax_amount}")
        print(f"Grand Total with Tax: ₹{total_with_tax}")
    except Exception:
        print("Invalid input! Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
