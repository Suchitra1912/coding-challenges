# Coding Challenge 35: Printing * Increasing Pattern (N Rows)
# *
# **
# ***
# ****
# ...
# N rows

def print_star_pattern(n):
    if n <= 0:
        return "Error"

    pattern = []
    for i in range(1, n + 1):
        pattern.append("*" * i)

    return pattern
