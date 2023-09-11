#!/usr/bin/python3
"""
A class tha describes my int
"""


class MyInt(int):
    """
    a class that describes my int
    """
    def __eq__(self, value):
        return not super().__eq__(value)

    def __ne__(self, value):
        return not super().__ne__(value)
