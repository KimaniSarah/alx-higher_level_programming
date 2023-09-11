#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Args:
        obj: the object to check if its an exact instance
        a_class: the class we are checking the object
    Return:
        True if the object is exactly an instance of the specified class
    """
    return issubclass(type(obj), a_class)
