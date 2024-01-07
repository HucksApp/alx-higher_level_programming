#!/usr/bin/python3

"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix: list, div: int | float) -> list:
    """Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """
    size = len(matrix[0])
    div_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for shape in matrix:
        shape_matrix = []
        if len(shape) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in shape:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError\
                ("matrix must be a matrix (list of lists) of integers/floats")
            shape_matrix.append(round(elem/div, 2))
        div_matrix.append(shape_matrix)
    return div_matrix

