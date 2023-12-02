# file for dynamic approach

# this dynamic approach is based on Kadane's algorithm

# The first step consist in  computing the max sub-array sum for a 1 dimension array

# This function return a tuple of the indices and the result of the sum (i, j, sum)


A = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1],

     [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

B = [[5, 6, 1, 4, 20], [8, -3, 9, 7, 6],
     [7, 8, 10, 5, 5], [4, 1, 5, 7, 6]]


def maxSubArraySum(A):
    max_current = A[0]
    max = A[0]
    first_index = last_index = temp_index = 0

    for i in range(1, len(A)):
        if A[i] > max_current + A[i]:
            temp_index = i
            max_current = A[i]
        else:
            max_current += A[i]

        if max_current > max:
            first_index = temp_index
            last_index = i
            max = max_current
    return first_index, last_index, max

# This function compute the max subarray for each column (considered as an array)
# Then update all the indices if the sum increases


def maxSumMatrix(M):
    nb_rows = len(M)
    nb_col = len(M[0])
    max_sum = 0
    max_up = max_down = max_left = max_right = -1
    for i in range(nb_col):
        temp_array = [0]*nb_rows
        for j in range(i, nb_col):
            for k in range(nb_rows):
                temp_array[k] += M[k][j]

            tpmaxup, tpmaxdown, current_sum = maxSubArraySum(temp_array)
            if current_sum > max_sum:
                max_sum = current_sum
                max_up = tpmaxup
                max_down = tpmaxdown
                max_left = i
                max_right = j

    return max_up, max_down, max_left, max_right, max_sum


solution = maxSumMatrix(A)

print("Max sum for A : {}, coord {} ".format(
    solution[4], (solution[0], solution[1], solution[2], solution[3])))
print(A[0])
print(A[1])
print(A[2])
print(A[3])
solution2 = maxSumMatrix(B)

print("Max sum for B : {}, coord {} ".format(
    solution2[4], (solution2[0], solution2[1], solution2[2], solution2[3])))
print(B[0])
print(B[1])
print(B[2])
print(B[3])
