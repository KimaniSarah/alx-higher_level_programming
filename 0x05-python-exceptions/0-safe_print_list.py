#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
        print()
    except IndexError:
        pass
    return printed
