#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[e ** 2 for e in row] for row in matrix]
    return new_matrix
