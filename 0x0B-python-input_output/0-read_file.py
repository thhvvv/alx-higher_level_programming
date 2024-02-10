#!/usr/bin/python3
"""function that reads a text file(UTF-8) and prints it in stdout"""

def read_file(filename=""):

    with open(filename, encoding = "utf-8") as f:
        print(f.read(), end = "")
