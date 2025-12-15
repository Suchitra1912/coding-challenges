def series_23(n: int) -> list[int]:
    """
    Generate the series: 1, 5, 9, 13, 21...
    """
    if n <= 0:
        raise ValueError("N must be positive")

    series = [1]
    diffs = [4, 4, 4, 8]  # Based on series pattern

    while len(series) < n:
        if len(series) - 1 < len(diffs):
            next_val = series[-1] + diffs[len(series) - 1]
        else:
            # Continue pattern by doubling the last difference
            next_val = series[-1] + (series[-1] - series[-2]) * 2
        series.append(next_val)

    return series[:n]
