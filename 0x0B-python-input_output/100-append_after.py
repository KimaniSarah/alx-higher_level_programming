#!/usr/bin/python3
"""define the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
     inserts a line of text to a file,
     after each line containing a specific string
     Args:
        filename:the file we are inserting the text
        search_string:the text that tells to insert a new line after its line
        new_string:the text to insert
    Returns:the updated text file
    """
    with open(filename, "r+", encoding="utf-8") as f:
        while f.readline() != "":
            line = f.readline()
            if search_string in line:
                f.write(new_string)
