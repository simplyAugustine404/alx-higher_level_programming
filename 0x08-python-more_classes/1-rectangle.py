#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle of width width and height height"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
        width(int): The width of the rectangle
        height(int): The height of the triangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the triangle"""
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
