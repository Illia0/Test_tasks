import random

def create_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix_line = []
        for j in range(n):
            matrix_line.append(random.randint(0,1))
        matrix.append(matrix_line)
    return matrix

def num_iland(matrix, line, column):
    count = 0
    for i in range(line):
        for j in range(column):
            if matrix[i][j] == 1:
                count += 1
                find_iland(matrix, i, j)
    return count


def find_iland(matrix, line, column):
    matrix[line][column] = 2
    matrix_line = len(matrix) - 1
    matrix_column = len(matrix[0]) - 1
    if column + 1 <= matrix_column:
        if matrix[line][column + 1] == 1:
            find_iland(matrix, line, column + 1)
    if column - 1 >= 0:
        if matrix[line][column - 1] == 1:
            find_iland(matrix, line, column - 1)
    if line + 1 <= matrix_line:
        if matrix[line + 1][column] == 1:
            find_iland(matrix, line + 1, column)
    if line - 1 >= 0:
        if matrix[line - 1][column] == 1: find_iland(matrix, line - 1, column)


if __name__ == '__main__':
    print("Input M,N for matrix:")
    try:
        line = int(input())
        column = int(input())
        matrix = create_matrix(line, column)
        for i in matrix:
            print(i)
        print("Num of ilands:", num_iland(matrix, line, column))
    except ValueError:
        print("Incorrect data")