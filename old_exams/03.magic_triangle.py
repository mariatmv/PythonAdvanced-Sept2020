def get_magic_triangle(n):
    matrix = []
    for i in range(1, n + 1):
        matrix.append([1]*i)

    for row in range(2, len(matrix)):
        for col in range(1, len(matrix[row]) - 1):
            matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]

    print(matrix)


get_magic_triangle(5)