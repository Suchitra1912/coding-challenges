"""
Retail Shopping Application – Hackathon
Author: Your Name
Date: YYYY-MM-DD
Description:
    Handles item entry, calculations of totals, discounts, surcharges, and invoice generation.
"""

# Store items in a dictionary
items = {}

def add_item(name: str, price: float, quantity: int) -> None:
    """
    Adds an item to the shopping cart.
    """
    if price < 0 or quantity <= 0:
        raise ValueError("Price must be non-negative and quantity positive.")
    items[name] = {"price": price, "quantity": quantity}

def calculate_total() -> float:
    """
    Calculates the total amount before discounts and surcharges.
    """
    return sum(info["price"] * info["quantity"] for info in items.values())

def apply_discount(total: float, discount_percentage: float) -> float:
    """
    Applies a percentage discount to the total.
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    return total * (1 - discount_percentage / 100)

def generate_invoice(discount: float = 0.0) -> dict:
    """
    Generates a detailed invoice with totals and discounts applied.
    """
    total = calculate_total()
    discounted_total = apply_discount(total, discount)
    return {
        "Items": items,
        "Total Before Discount": total,
        "Discount Percentage": discount,
        "Total After Discount": discounted_total
    }

# Optional: add more functions for membership discounts, surcharges, etc.
