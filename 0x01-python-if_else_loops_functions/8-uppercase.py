#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        uppercase_string += char
    print("{}".format(uppercase_string))
