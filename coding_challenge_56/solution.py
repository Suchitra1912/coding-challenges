def sum_2d_array(matrix):
    """
    Returns the sum of all elements in a 2D array.
    """
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total


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

        result = sum_2d_array(matrix)
        print("Sum of all elements in the 2D array:", result)
