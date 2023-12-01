# file for dynamic approach

# this dynamic approach is based on Kadane's algorithm

# The first step consist in  computing the max sub-array sum for a 1 dimension array

# This function return a tuple of the indices and the result of the sum (i, j, sum)

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


A = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1],

     [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

i1, i2, j1, j2, resofsum = maxSumMatrix(A)

print('i1 : {}, i2 : {}, j1 : {}, j2 : {}, sum : {}'.format(
    i1, i2, j1, j2, resofsum))
