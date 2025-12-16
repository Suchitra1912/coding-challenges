def count_odd_even(arr):
    """
    Returns the count of odd and even numbers in the array.
    """
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    if n <= 0:
        print("Array must contain at least one element.")
    else:
        print("Enter elements:")
        for _ in range(n):
            arr.append(int(input()))

        odd, even = count_odd_even(arr)
        print("Number of odd elements:", odd)
        print("Number of even elements:", even)
