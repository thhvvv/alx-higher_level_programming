#!/usr/bin/python3
"""defines base geoometry class"""

class BaseGeometry:

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
