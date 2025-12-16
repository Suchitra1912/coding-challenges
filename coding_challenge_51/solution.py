def store_elements(n, elements):
    """
    Stores n elements into an array and returns it.
    """
    if n <= 0:
        raise ValueError("Size of array must be positive")
    if len(elements) != n:
        raise ValueError("Number of elements must match n")
    return elements


if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = []

    if n <= 0:
        print("Array size must be greater than zero.")
    else:
        print("Enter elements:")
        for _ in range(n):
            arr.append(int(input()))

        result = store_elements(n, arr)
        print("Stored array:", result)
