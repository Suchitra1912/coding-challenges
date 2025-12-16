def print_number_pattern(n: int) -> list:
    # Validate input
    if n <= 0:
        raise ValueError("N must be a positive integer.")

    pattern = []

    # Generate pattern: each row contains the row number repeated N times
    for i in range(1, n + 1):
        pattern.append(str(i) * n)

    return pattern


# Run when executed directly
if __name__ == "__main__":
    N = int(input("Enter number of rows: "))
    for line in print_number_pattern(N):
        print(line)
