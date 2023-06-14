#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for h in my_list:
        if h == search:
            idx = new_list.index(h)
            new_list[idx] = replace
    return new_list
