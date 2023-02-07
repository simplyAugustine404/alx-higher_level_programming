#!/usr/bin/python3
"""Working with a rectangle"""


class Rectangle:
    """Defines a rectangle, its parameters, area and perimeter"""
    def __init__(self, width=0, height=0):
        """Initializes the values of a rectangle
        args:
        width(int):width of the rectangle
        height(int):height of the rectang;le
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets/gets the rectangles width"""
        return self.__width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Sets/gets the rectangles width"""
        return self.__height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """To print the rectangle with the '#' symbol"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            pieces = []
            for i in range(self.height):
                pieces.append("#" * self.width)
            return "\n".join(pieces)
