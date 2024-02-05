#!/usr/bin/python3
"""Create subclass of rectangle"""

rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """instantiate with size private inst attribute"""

        self.integer_validator("size", size)
        self.__size = size

        def area(self):

            return self.__size ** 2
