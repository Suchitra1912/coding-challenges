def display_series_17(n: int) -> list:
    """
    Generates a series from 1 to N.

    Parameters:
        n (int): The upper limit of the series.

    Returns:
        list: A list containing the series from 1 to N.
    """
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    return list(range(1, n + 1))
