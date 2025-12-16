def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    Returns index of target if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    if n <= 0:
        print("Array must contain at least one element.")
    else:
        print("Enter elements in sorted order:")
        for _ in range(n):
            arr.append(int(input()))

        key = int(input("Enter element to search: "))

        index = binary_search(arr, key)

        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found")
