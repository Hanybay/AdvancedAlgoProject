

def findtheoricbound(A):
    width = len(A[0])
    height = len(A)
    positiv = 0
    negativ = 0
    max = float('-inf')
    min = float('inf')
    n_positiv = 0
    m_negativ = 0
    for i in range(height):
        for j in range(width):
            if A[i][j] > max:
                max = A[i][j]
            if A[i][j] < min:
                min = A[i][j]
            if A[i][j] > 0:
                positiv += A[i][j]
                n_positiv += 1
            if A[i][j] < 0:
                negativ += A[i][j]
                m_negativ += 1
    mean_neg = abs(negativ)/m_negativ
    mean_pos = positiv/n_positiv

    return max, min, positiv, abs(negativ), mean_pos, mean_neg


def calculate_submatrix_sum(matrix, start_row, start_col, height, width):

    submatrix_sum = sum(sum(row[start_col:start_col + width])
                        for row in matrix[start_row:start_row + height])
    return submatrix_sum


A = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1],

     [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

B = [[5, 6, -1, -4, -20], [-8, -3, 9, 7, 6],
     [7, 8, 10, 5, 5], [-4, -1, 5, 7, -6]]


def calculate_all_submatrix_sums(matrix, height, width):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrix_sums = []

    for i in range(rows - height + 1):
        for j in range(cols - width + 1):
            start_row = i
            start_col = j
            submatrix_sum = calculate_submatrix_sum(
                matrix, start_row, start_col, height, width)

            # Ajoute une liste à la liste principale
            submatrix_sums.append([start_row, start_col, submatrix_sum])

    return submatrix_sums


def maxsubmatrixsum(matrix):
    max, min, sumpositiv, sumnegativ, mean_positiv, mean_negativ = findtheoricbound(
        matrix)

    width = len(matrix[0])
    height = len(matrix)
    boundwidth = width//2
    boundheight = height//2
    tmpmaxsum = -1000
    if mean_positiv > mean_negativ:

        for i in range(height-1, 0, -1):
            for j in range(width-1, 0, -1):
                temp_res = calculate_all_submatrix_sums(
                    matrix, boundheight+i, boundwidth+j)

    else:

        for i in range(boundheight):
            for j in range(boundwidth):
                temp_res = calculate_all_submatrix_sums(
                    matrix, i, j)

    print(temp_res)


maxsubmatrixsum(A)
maxsubmatrixsum(B)
