#!/usr/bin/python3
"""define the function from_json_string"""
import json


def from_json_string(my_str):
    """
    gives  object (Python data structure) represented by a JSON string
    Args:
        str:the string to returned as an object
    Return:
        str: object (Python data structure) represented by a JSON string:
    """
    python_obj = json.loads(my_str)
    return python_obj
