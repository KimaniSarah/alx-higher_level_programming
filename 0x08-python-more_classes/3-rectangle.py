#!/usr/bin/python3
"""defins a rectangle"""


class Rectangle:
    """start of rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize a new object
        args:
        width:size of short side
        height:size of the ling side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gives the area of the retangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height + self.__width + self.__height)

    def __str__(self):
        """prints the triangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_list = []
        for i in range(self.__height):
            [rectangle_list.append('#') for k in range(self.__width)]
            if i != self.__height - 1:
                rectangle_list.append("\n")
        return "".join(rectangle_list)
