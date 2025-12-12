from typing import Tuple

def sum_and_average(a: float, b: float) -> Tuple[float, float]:
    """Return sum and average of two numbers."""
    # Validate inputs
    for name, val in (("a", a), ("b", b)):
        if not isinstance(val, (int, float)):
            raise ValueError(f"{name} must be a number")
        if val != val:
            raise ValueError(f"{name} is NaN")
        if val in (float("inf"), float("-inf")):
            raise ValueError(f"{name} cannot be infinity")

    s = a + b
    avg = s / 2
    return s, avg

# ✅ This block runs the program interactively
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    total, average = sum_and_average(a, b)
    print("Sum:", total)
    print("Average:", average)
