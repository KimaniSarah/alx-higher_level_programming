#!/usr/bin/python3
""" returns True if the object is exactly an
instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """
    Args:
        obj: the object to check if its an exact instance
        a_class: the class we are checking the object
    Return:
        True if the object is exactly an instance of the specified class
    """
    return isinstance(obj, a_class)
