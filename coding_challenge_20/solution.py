def display_series_20(n: int) -> list:
    """
    Generates a series where each term is the previous term plus an incrementing integer starting from 1.

    Parameters:
        n (int): The number of terms in the series.

    Returns:
        list: A list containing the series up to the Nth term.
    """
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    
    series = []
    current_value = 1
    increment = 1
    
    for _ in range(n):
        series.append(current_value)
        current_value += increment
        increment += 1
    
    return series
