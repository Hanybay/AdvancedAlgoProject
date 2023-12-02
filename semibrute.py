

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

    return mean_pos, mean_neg


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

    for i in range(rows - width + 1):
        for j in range(cols - height + 1):
            start_row = i
            start_col = j
            if start_row != 0 and start_col != 0:
                submatrix_sum = calculate_submatrix_sum(
                    matrix, start_row, start_col, height, width)

            # Ajoute une liste à la liste principale
                submatrix_sums.append(
                    [start_row, start_col, height, width, submatrix_sum])

    return submatrix_sums


def maxsubmatrixsum(matrix):
    mean_positiv, mean_negativ = findtheoricbound(
        matrix)

    width = len(matrix[0])
    height = len(matrix)
    boundwidth = width//2
    boundheight = height//2
    tmpmaxsum = -1000
    temp_res = []
    if mean_positiv > mean_negativ:
        print("we there")
        for i in range(height-1, 1, -1):
            for j in range(width-1, 1, -1):
                temp_res.append(calculate_all_submatrix_sums(
                    matrix, boundheight+i-1, boundwidth+j-1))

    else:
        print("we here")
        for i in range(1, boundheight, 1):
            for j in range(1, boundwidth, 1):
                temp_res.append(calculate_all_submatrix_sums(
                    matrix, i, j))

    print(temp_res)
    for k in temp_res:
        for l in k:
            if l[4] > tmpmaxsum:
                tmpmaxsum = l[4]
                result = l

    return result


solution = maxsubmatrixsum(A)

print("Max sum for A : {}, coord {} ".format(
    solution[4], (solution[0], solution[1], solution[2], solution[3])))
print(A[0])
print(A[1])
print(A[2])
print(A[3])
solution2 = maxsubmatrixsum(B)

print("Max sum for B : {}, coord {} ".format(
    solution2[4], (solution2[0], solution2[1], solution2[2], solution2[3])))
print(B[0])
print(B[1])
print(B[2])
print(B[3])
