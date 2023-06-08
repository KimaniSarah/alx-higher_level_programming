#!/usr/bin/python3
for h in range(10):
    for v in range(1, 10):
        if h > v or h == v:
            continue
        elif h == 8 and v == 9:
            print("{0}{1}".format(h, v))
        else:
            print("{0}{1}".format(h, v), end=", ")
