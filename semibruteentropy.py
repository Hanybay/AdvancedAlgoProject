
import numpy as np
import math


def calculate_submatrix_sum(matrix, start_row, start_col, height, width):
    res = 0
    for i in range(height):
        for j in range(width):
            res += matrix[start_row+i][start_col+j]

    submatrix_sum = sum(sum(row[start_col:start_col + width])
                        for row in matrix[start_row:start_row + height])
    return res


A = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1],

     [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

B = [[5, 6, 1, 4, 20], [8, -3, 9, 7, 6],
     [7, 8, 10, 5, 5], [4, 1, 5, 7, 6]]

C = [[-1, -1, -1],
     [1, 1, 1],
     [-1, 1, 1]]


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

            # Ajoute une liste à la liste principale
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
    entropy = calculate_normalized_sign_entropy(matrix)
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


def calculate_normalized_sign_entropy(matrix):
    # Flatten the matrix to a 1D list
    values = [value for row in matrix for value in row]

    # Count the occurrences of each sign (positive/negative)
    sign_counts = {"positive": 0, "negative": 0}

    for value in values:
        if value > 0:
            sign_counts["positive"] += 1
        elif value < 0:
            sign_counts["negative"] += 1

    # Calculate entropy
    entropy = 0
    total_values = len(values)

    for count in sign_counts.values():
        probability = count / total_values
        if probability > 0:
            entropy -= probability * math.log2(probability)

    # Calculate maximum possible entropy
    max_entropy = -sum((count / total_values) * math.log2(count / total_values)
                       for count in (total_values / 2, total_values / 2))

    # Normalize entropy between 0 and 1
    normalized_entropy = entropy / max_entropy

    return normalized_entropy


def calculate_sign_entropy(matrix):
    # Flatten the matrix to a 1D list
    values = [value for row in matrix for value in row]

    # Count the occurrences of each sign (positive/negative)
    sign_counts = {"positive": 0, "negative": 0}

    for value in values:
        if value > 0:
            sign_counts["positive"] += 1
        elif value < 0:
            sign_counts["negative"] += 1

    # Calculate entropy
    entropy = 0
    total_values = len(values)

    for count in sign_counts.values():
        probability = count / total_values
        if probability > 0:
            entropy -= probability * math.log2(probability)

    return entropy


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

solution2 = maxsubmatrixsum(C)

print("Max sum for C: {}, coord {} ".format(
    solution2[4], (solution2[0], solution2[1], solution2[2], solution2[3])))
print(C[0])
print(C[1])
print(C[2])
