#!/usr/bin/python3

"""divides all elementa of a matrix"""


def matrix_divided(matrix, div):
    """"
    a function that divides all elements of a matrix.
    args:
    matrix:list of lists of integers or floats
    div: a number (integer or float)
    Returns: a new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a(list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    first_row_size = len(matrix[0])
    if any(len(row) != first_row_size for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(ele / div, 2) for ele in row] for row in matrix]
    return new_matrix
