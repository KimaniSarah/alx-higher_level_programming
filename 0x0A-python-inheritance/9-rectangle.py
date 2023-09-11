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

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        result = self.__width * self.__height
        return result
