def separate_whole_fraction(value: float) -> tuple[int, float]:
    whole = int(value)
    fraction = value - whole
    return whole, fraction

if __name__ == "__main__":
    val = float(input("Enter a decimal number: "))
    w, f = separate_whole_fraction(val)
    print("Whole part:", w)
    print("Fractional part:", f)
