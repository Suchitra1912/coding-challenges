def multiply_matrices(A, B):
    """
    Multiplies two matrices A and B and returns the result.
    """
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix multiplication not possible")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def display_matrix(matrix):
    """
    Displays matrix row-wise.
    """
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    r1 = int(input("Enter rows of first matrix: "))
    c1 = int(input("Enter columns of first matrix: "))

    print("Enter elements of first matrix:")
    matrix1 = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        matrix1.append(row)

    r2 = int(input("Enter rows of second matrix: "))
    c2 = int(input("Enter columns of second matrix: "))

    print("Enter elements of second matrix:")
    matrix2 = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        matrix2.append(row)

    try:
        product = multiply_matrices(matrix1, matrix2)
        print("\nResultant Matrix:")
        display_matrix(product)
    except ValueError as e:
        print(e)
