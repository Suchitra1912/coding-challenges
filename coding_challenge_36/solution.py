# Coding Challenge 36: Printing number Increasing Pattern (N Rows)
# Pattern:
# 1
# 22
# 333
# ...
# N rows

def number_increasing_pattern(n):
    if n <= 0:
        return "Error"

    pattern = []
    for i in range(1, n + 1):
        pattern.append(str(i) * i)

    return pattern
