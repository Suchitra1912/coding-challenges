"""
Coding Challenge 28: Membership Discounts
Objective: Apply an additional 2% discount for members.
"""

def apply_membership_discount(grand_total: float, is_member: str) -> float:
    """
    Apply membership discount if the customer is a member.

    Parameters:
        grand_total (float): Total amount before membership discount
        is_member (str): 'y' if member, 'n' if not

    Returns:
        float: Grand total after membership discount
    """
    if is_member.lower() == 'y':
        return round(grand_total * 0.98, 2)  # 2% discount
    return grand_total


def main():
    try:
        grand_total = float(input("Enter the grand total: ₹"))
        is_member = input("Is the customer a member? (y/n): ")
        final_total = apply_membership_discount(grand_total, is_member)
        print(f"Final Grand Total: ₹{final_total}")
    except Exception:
        print("Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    main()
