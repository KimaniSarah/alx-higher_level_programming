#!/usr/bin/python3
"""defines the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    Args:
        my_obj:the objct to rep in json and write into a file
        filename:the file to write into
    Return:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
