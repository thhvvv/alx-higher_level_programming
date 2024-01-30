#!/usr/bin/python3
"""defines a text-indentation function """

def text_indentation(text):
    """prints text with two new lines after each of the following characters '.', '?', ':'."""

    if not isinstance(text, str):
        raise TypeErrror("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
                c += 1
                while c < len(text) and text[c] == ' ':
                    c += 1
                continue
            c += 1
