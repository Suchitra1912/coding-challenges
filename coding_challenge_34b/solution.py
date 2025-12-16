# Coding Challenge 34: Printing Number Pattern (N Rows)
# Objective:
# Print the following pattern for N rows:
# 12345
# 12345
# 12345
# 12345
# .
# .
# N rows

def print_number_pattern(n: int) -> list:
    if n <= 0:
        raise ValueError("N must be a positive integer.")

    pattern = []
    row = "".join(str(i) for i in range(1, n + 1))

    for _ in range(n):
        pattern.append(row)

    return pattern


if __name__ == "__main__":
    N = int(input("Enter number of rows: "))
    for line in print_number_pattern(N):
        print(line)
