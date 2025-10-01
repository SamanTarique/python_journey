"""Hard"""

"""https://edabit.com/challenge/DC2s6hM8yE7RvBr3S"""


def subtract_matrix(matrix1, matrix2):
    res_matrix = []

    for i in range(len(matrix1)):
        temp_matrix = []
        for j in range(len(matrix2)):
            temp_matrix.append(matrix1[i][j] - matrix2[i][j])
        res_matrix.append(temp_matrix)
    return res_matrix


print(
    subtract_matrix(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
)
