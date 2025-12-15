def series_24(n: int) -> list[int]:
    """Generate Fibonacci series up to N elements."""
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    result = [1]
    if n == 1:
        return result
    result.append(1)
    for i in range(2, n):
        result.append(result[-1] + result[-2])
    return result
