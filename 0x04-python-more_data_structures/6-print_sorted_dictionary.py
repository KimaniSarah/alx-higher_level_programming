#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_key = sorted(a_dictionary.keys())
    for h in sort_key:
        value = a_dictionary[h]
        print("{}: {}".format(h, value))
