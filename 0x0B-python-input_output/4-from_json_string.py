#!/usr/bin/python3
"""an object represented by a JSON string"""
import json

def from_json_string(my_str):
    return json.loads(my_str)
