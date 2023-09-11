#!/usr/bin/python3
"""
a class base geometry
"""


class BaseGeometry:
    """
    a class with one method
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 1:
            raise ValueError("<name> must be greater than 0")
