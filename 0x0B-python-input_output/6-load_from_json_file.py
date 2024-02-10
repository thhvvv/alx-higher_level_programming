#!/usr/bin/python3
"""creates an object from a JSON file"""
import json

def load_from_json_fie(filename):
    with open(filename, 'r') as f:
        return json.load(f)
