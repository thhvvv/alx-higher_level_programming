#!/usr/bin/python3
"""class that defines rectangle"""


class Rectangle:
    """ a class that defines Rectangle
        Args: width of type int
              height of type int"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instances for width and height """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """deletes an instsnce of class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ set the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ properties of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ set the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ properties of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """returns a rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
            for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """string representation to create new instances"""
        return ("Rectangle({:d}, {:d}".format(self.width, self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new Rectangle with width == height == size """
        return cls(size, size)
