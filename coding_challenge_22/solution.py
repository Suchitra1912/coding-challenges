def series_22(n: int) -> list[int]:
    """
    Generate the series: 1, 4, 7, 11, 18...
    """
    if n <= 0:
        raise ValueError("N must be positive")

    series = [1]
    diff = 3  # initial difference
    next_diff = 3

    while len(series) < n:
        next_val = series[-1] + next_diff
        series.append(next_val)
        # Update next_diff: sum of previous two differences
        if len(series) == 2:
            next_diff = 3
        else:
            next_diff = series[-1] - series[-2] + series[-2] - series[-3]

    return series
