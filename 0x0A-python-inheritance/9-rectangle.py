#!/usr/bin/python3
"""defines class rectangle that inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Instantiation with width and height private inst attrs"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):

        return self.__width * self.__height
