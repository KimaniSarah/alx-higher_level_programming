#!/usr/bin/python3
"""
a class base geometry
"""


class BaseGeometry:
    """
    a class with one method
    """
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


"""
a class base geometry
"""


class Rectangle(BaseGeometry):
    """
    a class with one method
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
