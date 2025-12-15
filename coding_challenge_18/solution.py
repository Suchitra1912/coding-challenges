def display_series_18(n: int) -> list:
    """
    Generates a series of odd numbers starting from 1 up to the largest odd number ≤ N.

    Parameters:
        n (int): The upper limit of the series.

    Returns:
        list: A list containing the series of odd numbers up to N.
    """
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    return [i for i in range(1, n + 1) if i % 2 != 0]
