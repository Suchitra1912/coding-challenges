# Coding Challenge 38: Fibonacci Series Pattern (N Rows)
# Pattern:
# 1
# 1 2
# 3 5 8
# 13 21 34 55
# ...
# N rows

def fibonacci_pattern(n):
    if n <= 0:
        return "Error"

    fib = [1, 1]
    for i in range(2, n * (n + 1) // 2):
        fib.append(fib[-1] + fib[-2])

    result = []
    index = 0
    for row in range(1, n + 1):
        current_row = fib[index:index + row]
        result.append(" ".join(map(str, current_row)))
        index += row

    return result
