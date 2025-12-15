def star_pattern(n: int) -> list:
    """
    Generates a star pattern with N rows.
    Args:
        n (int): Number of rows (must be positive).
    Returns:
        list: List of strings, each string represents a row of stars.
    Raises:
        ValueError: If n is not positive.
    """
    if not isinstance(n, int):
        raise TypeError("Number of rows must be an integer.")
    if n <= 0:
        raise ValueError("Number of rows must be positive.")
    return ['*' * n for _ in range(n)]
