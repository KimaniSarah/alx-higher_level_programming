#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for h in my_string:
        if h.upper() != 'C':
            new_string += h
    return new_string
