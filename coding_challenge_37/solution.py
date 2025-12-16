# Coding Challenge 37: Printing number Increasing Pattern (N Rows)
# Pattern:
# 1
# 12
# 123
# ...
# N rows

def number_increasing_pattern(n):
    if n <= 0:
        return "Error"

    pattern = []
    for i in range(1, n + 1):
        row = "".join(str(num) for num in range(1, i + 1))
        pattern.append(row)

    return pattern
