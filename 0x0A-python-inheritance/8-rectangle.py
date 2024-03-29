#!/usr/bin/python3
"""
a class base geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
