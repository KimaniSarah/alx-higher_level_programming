#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("{} argument{}.".format(argc, 's' if argc != 1 else ''))
    else:
        print("{} argument{}:".format(argc, 's' if argc != 1 else ''))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
