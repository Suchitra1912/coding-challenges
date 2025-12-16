# Coding Challenge 40: Printing Pattern of Factorials in N Rows

from math import factorial

def factorial_pattern(n):
    pattern = []
    for i in range(1, n+1):
        row = [factorial(j) for j in range(1, i+1)]
        pattern.append(row)
    return pattern

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in factorial_pattern(n):
        print(' '.join(map(str, row)))
