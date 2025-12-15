def display_series_19(n: int) -> list:
    """
    Generates a series of squares of even numbers starting from 2 up to the largest even number ≤ N.

    Parameters:
        n (int): The upper limit of the series.

    Returns:
        list: A list containing the squares of even numbers up to N.
    """
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    return [i**2 for i in range(2, n + 1, 2)]
