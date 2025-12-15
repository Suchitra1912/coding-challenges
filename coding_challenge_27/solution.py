"""
Coding Challenge 27: Applying Discounts
"""

def apply_discounts(grand_total: float, total_quantity: int) -> float:
    """
    Apply discounts based on total amount and quantity.

    Parameters:
        grand_total (float): Total cost of all items
        total_quantity (int): Total number of items

    Returns:
        float: Discounted total
    """
    if grand_total > 10000:
        grand_total *= 0.9  # 10% discount
    if total_quantity > 20:
        grand_total *= 0.95  # Additional 5% discount
    return round(grand_total, 2)
