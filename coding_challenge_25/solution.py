"""
Coding Challenge 25: Basic Item Entry and Total Calculation
Author: Your Name
Date: YYYY-MM-DD
Description:
    Accept item details and calculate total cost.
"""

def calculate_item_total(code: str, description: str, quantity: int, price: float) -> dict:
    """
    Calculate total cost for a single item.

    Parameters:
        code (str): Item code
        description (str): Item description
        quantity (int): Quantity of the item
        price (float): Price per unit

    Returns:
        dict: Contains item details and total cost
    """
    if quantity < 0 or price < 0:
        raise ValueError("Quantity and price must be non-negative.")
    total = quantity * price
    return {"Code": code, "Description": description, "Quantity": quantity, "Price": price, "Total": total}


def main():
    try:
        code = input("Enter item code: ")
        description = input("Enter item description: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        item = calculate_item_total(code, description, quantity, price)
        print(f"\nItem Total: {item['Total']}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
