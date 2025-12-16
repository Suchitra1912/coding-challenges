def create_matrix(rows, cols, elements):
    """
    Creates an M x N matrix from the given elements.
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


def transpose_matrix(matrix):
    """
    Returns the transpose of the given matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose


def display_matrix(matrix):
    """
    Displays the matrix row-wise.
    """
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    rows = int(input("Enter number of rows (M): "))
    cols = int(input("Enter number of columns (N): "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be greater than zero.")
    else:
        elements = []
        print("Enter elements row-wise:")
        for _ in range(rows * cols):
            elements.append(int(input()))

        matrix = create_matrix(rows, cols, elements)

        print("\nMatrix:")
        display_matrix(matrix)

        transpose = transpose_matrix(matrix)

        print("\nTranspose of the matrix:")
        display_matrix(transpose)
