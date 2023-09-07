#!/usr/bin/python3

""" prints a square with the character #."""


def print_square(size):
    """
    prints a square with the character
    Args:
    size: size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        for _ in range(size):
            print("#", end="")
        print()
