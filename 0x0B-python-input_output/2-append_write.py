#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    Args:
        filename:the file to append the text into
        text:the string to append into the file
    Return:
        int:number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as f:
        no_of_chars_added = f.write(text)
        return no_of_chars_added
