#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    arguments = len(arg)
    sum = 0
    for h in range(1, arguments):
        sum += int(arg[h])
    print("{}".format(sum))
