#!/usr/bin/python3
"""define the function pascal_triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Args:
        n: no of rows
    Return: a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    for num in range(n):
        row = [1]

        if num > 0:
            prev_row = triangle[-1]
            for i in range(1, num):
                row.append(prev_row[i - 1] + prev_row[i])
            row.append(1)
        triangle.append(row)
    return triangle
