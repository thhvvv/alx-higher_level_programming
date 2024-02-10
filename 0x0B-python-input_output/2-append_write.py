#!/usr/bin/python3
"""appends a string of a textfile"""

def append_write(filename="", text=""):
    with open(filename, 'a')as f:
        return f.write(text)
