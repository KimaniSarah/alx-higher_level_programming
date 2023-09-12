#!/usr/bin/python3


import json
""" gives the JSON representation of an object(string)"""


def to_json_string(my_obj):
    """
    gives a json rep of an object
    Args:
        my_obj:the object to be rep in json string
    Return:
        char: JSON representation of an object (string):
    """
    json_file = json.dumps(my_obj)
    return json_file
