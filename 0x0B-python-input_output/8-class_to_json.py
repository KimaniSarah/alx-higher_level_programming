#!/usr/bin/python3
"""defines the function class_t_json"""


def class_to_json(obj):
    """
    Generates a dictionary description for an
    object containing simple data structures.

    Args:
        obj: The input object to describe.

    Returns:
        dict: A dictionary representation of the object's structure.
    """
    return obj.__dict__
