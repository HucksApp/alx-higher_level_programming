#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""


    for matr in (m_a, m_b):
        msg = "m_a" if matr == m_a else "m_b"

        if matr == [] or matr == [[]]:
            raise ValueError(f"{msg} can't be empty")

        if type(matr) is not list:
            raise TypeError(f"{msg} must be a list")

        size = len(matr[0])
        for row in matr:
            if type(row) is not list:
                raise TypeError(f"{msg} must be a list of lists")

            if len(row) != size:
                raise TypeError(f"each row of {msg} must be of the same size")
            for x in row:
                if type(x) not in [int, float]:
                    raise TypeError(f"{msg} should contain only integers or floats")

    a_col = 0
    for col in m_a[0]:
        a_col += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
