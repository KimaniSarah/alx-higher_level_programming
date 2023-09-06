#!/usr/bin/python3


""""adds 2 integers."""


def add_integer(a, b=98):

    """checks if a and are either int or floats if not a TypeError is raised"""
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    """cases a and b into int if they are float"""
    a = int(a)
    b = int(b)

    """returns the sum of a and b"""
    return a + b
