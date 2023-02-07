#!/usr/bin/python3
"""Area and perimeter for a rectangle"""


class Rectangle:
    """Defines a rectangle, dimensions, are and perimeter"""

    def __init__(self, width=0, height=0):
        """Instantiates the width and height

        Args:
        width(int): width of rectangle
        height(int): height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        if value != int(value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        if value != int(value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the rectangles area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangles perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
