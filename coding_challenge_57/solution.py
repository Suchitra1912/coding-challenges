def element_exists(matrix, target):
    """
    Checks whether the target element exists in the 2D array.
    Returns True if found, otherwise False.
    """
    for row in matrix:
        for element in row:
            if element == target:
                return True
    return False


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be greater than zero.")
    else:
        matrix = []
        print("Enter elements row-wise:")
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(int(input()))
            matrix.append(row)

        target = int(input("Enter element to search: "))

        if element_exists(matrix, target):
            print("Element exists in the 2D array.")
        else:
            print("Element does not exist in the 2D array.")
