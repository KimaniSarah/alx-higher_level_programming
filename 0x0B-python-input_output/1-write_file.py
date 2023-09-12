#!/usr/bin/python3
""" writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    Args:
        filename:the file to write into
        text:the string to write into the file
    Return:
        returns the number of characters written:
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
