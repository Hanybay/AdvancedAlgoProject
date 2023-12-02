class MatrixMaxSegmentProblem:
    class Result:
        def __init__(self, max_sum, i1, i2, j1, j2):
            self.max_sum = max_sum
            self.i1 = i1
            self.i2 = i2
            self.j1 = j1
            self.j2 = j2

    @staticmethod
    def max_segment_sum(matrix, sub_matrix_rows, sub_matrix_cols):
        M = len(matrix)
        N = len(matrix[0])

        result = MatrixMaxSegmentProblem.Result(float('-inf'), -1, -1, -1, -1)

        for i1 in range(M - sub_matrix_rows + 1):
            for j1 in range(N - sub_matrix_cols + 1):
                i2 = i1 + sub_matrix_rows - 1
                j2 = j1 + sub_matrix_cols - 1

                # To calculate the sum for the current submatrix
                current_sum = MatrixMaxSegmentProblem.calculate_sum(matrix, i1, i2, j1, j2)

                # Update the result if the current sum is greater
                if current_sum > result.max_sum:
                    result.max_sum = current_sum
                    result.i1 = i1
                    result.i2 = i2
                    result.j1 = j1
                    result.j2 = j2

        return result

    @staticmethod
    def calculate_sum(matrix, i1, i2, j1, j2):
        total_sum = 0
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                total_sum += matrix[i][j]
        return total_sum


def main():
    print("Veuillez saisir la taille de la sous-matrice m * n: ")
    sub_matrix_size = input()
    dimensions = sub_matrix_size.split('*')
    sub_matrix_rows = int(dimensions[0])
    sub_matrix_cols = int(dimensions[1])

    matrix = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]

    result = MatrixMaxSegmentProblem.max_segment_sum(matrix, sub_matrix_rows, sub_matrix_cols)

    print("-------------------------------------")
    print("Maximum Segment Sum:", result.max_sum)
    print("-------------------------------------")
    print("Indices (i1, i2, j1, j2): \n\t",
          result.i1, ",", result.i2, ",", result.j1, ",", result.j2)
    print("-------------------------------------")


if __name__ == "__main__":
    main()
