#!/usr/bin/python3

def add_attribute(obj, name, value):

    """adds a new attribute to an object if its possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError
