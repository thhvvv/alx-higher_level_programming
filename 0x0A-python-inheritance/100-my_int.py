#!/usr/bin/python3

class MyInt(int):

    """MyInt class"""
    def __eq__(self, other):
        """equals method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """not equal method"""
        return super().__eq__(other)
