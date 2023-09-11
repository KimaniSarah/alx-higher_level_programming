#!/usr/bin/python3
""" checks  if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""

def inherits_from(obj, a_class):
    """
    Args:
        obj:the object we are checking
        a_class:the class that we are checking in
    Return: returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)

    for instance in type(obj).mro():
        if instance == a_class:
            return True
    return False

