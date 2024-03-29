#!/usr/bin/python3
"""defins a rectangle"""


class Rectangle:
    """start of rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize a new object
        args:
        width:size of short side
        height:size of the ling side
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        r_lst = []
        for i in range(self.__height):
            [r_lst.append(str(self.print_symbol)) for n in range(self.__width)]
            if i != self.__height - 1:
                r_lst.append("\n")
        return "".join(r_lst)

    def __repr__(self):
        """return a str rep of rectangle to be able to recreate a instance"""
        x = str(self.__width)
        y = str(self.__height)
        return "Rectangle(" + x + ", " + y + ")"

    def __del__(self):
        """detect instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1
