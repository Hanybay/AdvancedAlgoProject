# file for dynamic approach


def maxSubmatrixSumDC(matrix):

    # case if matrix dimensions are 1x1, return the
    nb_rows = len(matrix)
    nb_columns = len(matrix[0])
    if nb_rows == 1 and nb_columns == 1:
        return matrix[0][0]

    max_sum = -65659

    middle_row = nb_rows // 2
    middle_col = nb_columns // 2

    for i in range(2):
        for j in range(2):
            sub_matrix = [[0]*middle_col for x in range(middle_row)]

            for r in range(middle_row):
                for c in range(middle_col):
                    sub_matrix[r][c] = matrix[i *
                                              middle_row + r][j * middle_col + c]

            sum_sub_matrix = maxSubmatrixSumDC(sub_matrix)

            max_sum = max(max_sum, sum_sub_matrix)
    return max_sum


l = [
    [1, 2, -1],
    [-3, 0, 5],
    [3, 4, 2]
]
res = maxSubmatrixSumDC(l)
print("sum max of submatrix:", res)
