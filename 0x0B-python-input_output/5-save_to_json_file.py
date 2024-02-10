#!/usr/bin/python3
"""writes an object to a text file, using JSON representation"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
