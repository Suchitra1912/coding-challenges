def sort_array(arr, order):
    """
    Sorts the array in ascending or descending order.
    
    order: 'asc' for ascending, 'desc' for descending
    """
    if order == "asc":
        return sorted(arr)
    elif order == "desc":
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Invalid sort order. Use 'asc' or 'desc'.")


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    if n <= 0:
        print("Array must contain at least one element.")
    else:
        print("Enter elements:")
        for _ in range(n):
            arr.append(int(input()))

        order = input("Enter sorting order (asc/desc): ").lower()

        try:
            result = sort_array(arr, order)
            print("Sorted array:", result)
        except ValueError as e:
            print(e)
