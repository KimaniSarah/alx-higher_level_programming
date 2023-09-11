#!/usr/bin/python3
def lookup(obj):
    """
     list of available attributes and methods of an object
     Args:
         obj:The object for which to list attributes and methods
     Return:
        A list of attribute and method names.
    """
    return dir(obj)
