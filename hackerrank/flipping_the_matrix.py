def flippingMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0
    for i in range(0, rows // 2):
        for j in range(0, cols // 2):
            sum += max(
                matrix[i][j],
                matrix[i][cols - j - 1],
                matrix[rows - 1 - i][j],
                matrix[rows - 1 - i][cols - 1 - j],
            )

    return sum
