# Function to calculate loyalty points based on grand total
def calculate_loyalty_points(grand_total: float) -> int:
    """
    Calculates loyalty points: 1 point for every ₹100 spent.
    Args:
        grand_total (float): The final grand total of the purchase.
    Returns:
        int: Number of loyalty points earned.
    Raises:
        ValueError: If grand_total is negative.
    """
    if not isinstance(grand_total, (int, float)):
        raise TypeError("Grand total must be a number.")
    if grand_total < 0:
        raise ValueError("Grand total cannot be negative.")
    return int(grand_total // 100)
