#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    for h, char in enumerate(str):
        if h != n:
            new_str.append(char)
    return "".join(new_str)
