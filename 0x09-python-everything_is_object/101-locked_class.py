#!/usr/bin/python3
"""class definition"""
class LockedClass:
    """Clss that prevents user from dynamic attributes"""
    __slots__ = ['first_name']
