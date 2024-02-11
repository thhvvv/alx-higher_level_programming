#!/usr/bin/python3
"""appends a string of a textfile"""

def append_write(filename="", text=""):
    """ appends string and returns number of characters """
    
    string = 0
    with open(filename, "a", encoding="utf-8") as f:
        string = f.write(text)

    return string
