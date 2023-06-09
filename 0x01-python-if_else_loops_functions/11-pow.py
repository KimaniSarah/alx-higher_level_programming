#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        if b % 2 != 0:
            result *= a
        a *= a
        b >>= 1
    return "{:.2f}".format(result)
