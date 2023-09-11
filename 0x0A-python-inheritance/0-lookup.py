#!/usr/bin/python3
"""list of available attributes and methods of an object"""


def lookup(obj):
    """
     list of available attributes and methods of an object
     Args:
         obj:The object for which to list attributes and methods
     Return:
        A list of attribute and method names.
    """
    return dir(obj)
