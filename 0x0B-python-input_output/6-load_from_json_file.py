#!/usr/bin/python3
"""defines the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    Args:
        filename: the file we json file
    Return:
         object: The object obtained from the JSON data.
    """
    with open(filename, encoding="utf-8") as f:
        string = f.read()
        data = json.loads(string)
        return data
