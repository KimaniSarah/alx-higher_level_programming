#!/usr/bin/python3
class Square:

    """square class"""

    def __init__(self, size=0):
        """
        initialize a square instance
        Args:
            size(int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """
        returns value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """"
        sets the size of the square
        Args:
            value(int):the new value set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
