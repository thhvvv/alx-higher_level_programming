#!/usr/bin/python3
""" writes file module """


def write_file(filename="", text=""):
    
    string = 0
    with open(filename, "w", encoding="utf-8") as f:
        string = f.write(text)
        
    return string
