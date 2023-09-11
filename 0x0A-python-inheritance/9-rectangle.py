#!/usr/bin/python3
"""
A class representing a rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance.
        area(self): Computes and returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>"
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
