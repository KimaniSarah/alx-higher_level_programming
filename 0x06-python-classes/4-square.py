#!/usr/bin/python3

"""
Square Module
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
            size (int): Size of the square, defaults to 0
        """
        self.__size = size

    def size(self):
        """
        Retrieves the size of the square
        Returns:
            int: The size of the square
        """
        return self.__size

    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int): Size value to be set
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2
