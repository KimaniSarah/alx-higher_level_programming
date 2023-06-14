#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set()
    for h in my_list:
        new_list.add(h)
    sum_unique = sum(new_list)
    return sum_unique
