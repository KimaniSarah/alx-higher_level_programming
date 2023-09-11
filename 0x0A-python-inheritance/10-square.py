#!/usr/bin/python3

"""A class that represents a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square
    Attributes:
        __size(int):size of the square
    Methods:
        area:the area of the square
    """
    def __init__(self, size):
        """
        it initiates a square instance
        Args:
            size:the size of a square
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
