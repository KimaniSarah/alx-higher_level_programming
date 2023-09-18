#!/usr/bin/python3
"""defines the triangle class"""
import sys
from models.base import Base


class Rectangle(Base):
    """START A NEW RECTANGLE CLASS"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """INIT A NEW RECTANGLE
        ARGS
        ====
        width (int)
        height (int)
        x, y (int)
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set/Update the width value"""
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set/Update the height value"""
        self.__height = value

    @property
    def x(self):
        """Get the value of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set/Update the x value"""
        self.__x = value

    @property
    def y(self):
        """Get the value of the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set/Update the y value"""
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        results = self.__width * self.__height
        return results

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character # -
        you don’t need to handle x and y here
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle
        Arguments
        ==========
        1ST argument should be the ID attribute
        2ND argument should be the WIDTH attribute
        3RD argument should be the HEIGHT attribute
        4TH argument should be the X attribute
        5TH argument should be the Y attribute
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """DIC REPRESENTATION"""
        key_list = ['id', 'width', 'height', 'x', 'y']
        dict_result = {}
        for key in key_list:
            dict_result[key] = getattr(self, key)
        return dict_result

    def __str__(self):
        """STR DUNDER METHOS """
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)

        return str_rect + str_id + str_xy + str_w
