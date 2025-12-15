"""
Coding Challenge 21: Display Series 1,4,9,25,36,49,81...N
Author: Your Name
Date: YYYY-MM-DD
Description:
    Generate series of squares with a custom pattern until N.
"""

def series_21(n: int) -> list[int]:
    """Generate the series 1,4,9,25,36,49,81,... up to N elements."""
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result
