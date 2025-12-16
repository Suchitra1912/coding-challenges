def generate_series(n: int) -> list[int]:
    series = []
    current = 1
    sign = 1
    for i in range(n):
        series.append(current)
        current += 4 * sign
        sign *= -1
    return series

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print("Series:", generate_series(n))
