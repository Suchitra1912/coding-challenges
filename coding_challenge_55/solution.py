def create_2d_array(rows, cols, elements):
    """
    Creates and returns a 2D array using given elements.
    """
    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[index])
            index += 1
        matrix.append(row)

    return matrix


def display_row_wise(matrix):
    """
    Displays elements of 2D array row-wise.
    """
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be greater than zero.")
    else:
        elements = []
        print("Enter elements:")
        for _ in range(rows * cols):
            elements.append(int(input()))

        matrix = create_2d_array(rows, cols, elements)

        print("\n2D Array elements (row-wise):")
        display_row_wise(matrix)
