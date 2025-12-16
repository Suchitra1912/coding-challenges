def find_maximum(arr):
    """
    Returns the maximum value in the given array.
    """
    if not arr:
        raise ValueError("Array must not be empty")

    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    if n <= 0:
        print("Array must contain at least one element.")
    else:
        print("Enter elements:")
        for _ in range(n):
            arr.append(int(input()))

        result = find_maximum(arr)
        print("Maximum value in the array:", result)
