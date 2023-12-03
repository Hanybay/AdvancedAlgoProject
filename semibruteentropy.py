# Semi-brute-force (Version 2)
import numpy as np
import math


def calculate_entropy_array(array):

    maxserie = 0
    currentmaxserie = 0
    bitofsign = -1
    size = len(array)
    if size == 0:
        return

    for number in array:
        if bitofsign == -1:
            if number < 0:
                bitofsign = 0
                currentmaxserie += 1
            else:
                bitofsign = 1
                currentmaxserie += 1

                if currentmaxserie > maxserie:
                    maxserie = currentmaxserie
        elif (bitofsign == 0 and number < 0) or (bitofsign == 1 and number >= 0):
            currentmaxserie += 1
            if currentmaxserie > maxserie:
                maxserie = currentmaxserie
        else:
            currentmaxserie = 1
            bitofsign = (bitofsign + 1) % 2

    entropy = 1 - (maxserie / size)
    return entropy


def calculate_general_entropy_matrix(matrix):
    general_entropy = -1
    currententropy = 0
    for line in matrix:
        currententropy += calculate_entropy_array(line)
    general_entropy = currententropy / len(matrix)
    return general_entropy


def calculate_submatrix_sum(matrix, start_row, start_col, height, width):
    res = 0
    for i in range(height):
        for j in range(width):
            res += matrix[start_row+i][start_col+j]

    return res


def calculate_all_submatrix_sums(matrix, height, width):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrix_sums = []

    for i in range(rows - height+1):
        for j in range(cols - width+1):
            start_row = i
            start_col = j

            submatrix_sum = calculate_submatrix_sum(
                matrix, start_row, start_col, height, width)

            # add a list at the end of the main list
            submatrix_sums.append(
                [start_row, start_col, height, width, submatrix_sum])

    return submatrix_sums


def maxsubmatrixsum(matrix):

    width = len(matrix[0])
    height = len(matrix)
    boundwidth = width//2
    boundheight = height//2
    tmpmaxsum = -1000
    temp_res = []
    entropy = calculate_general_entropy_matrix(matrix)
    if entropy < 0.5:

        for i in range(height, boundheight, -1):
            for j in range(width, boundwidth, -1):
                temp_res.append(calculate_all_submatrix_sums(
                    matrix, i, j))

    else:

        for i in range(1, boundheight+2, 1):
            for j in range(1, boundwidth+2, 1):
                temp_res.append(calculate_all_submatrix_sums(
                    matrix, i, j))

    for k in temp_res:
        for l in k:
            if l[4] > tmpmaxsum:
                tmpmaxsum = l[4]
                result = l

    return result


A = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1],

     [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

B = [[5, 6, 1, 4, 20], [8, -3, 9, 7, 6],
     [7, 8, 10, 5, 5], [4, 1, 5, 7, 6]]


solution = maxsubmatrixsum(A)

print("Max sum for A : {}, coord {} ".format(
    solution[4], (solution[0], solution[1], solution[2], solution[3])))
print(A[0])
print(A[1])
print(A[2])
print(A[3])

print("Entropy of matrix A : {}".format(calculate_general_entropy_matrix(A)))
solution2 = maxsubmatrixsum(B)

print("Max sum for B : {}, coord {} ".format(
    solution2[4], (solution2[0], solution2[1], solution2[2], solution2[3])))
print(B[0])
print(B[1])
print(B[2])
print(B[3])
print("Entropy of matrix B : {}".format(calculate_general_entropy_matrix(B)))
