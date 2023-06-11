#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_4 = dir(hidden_4)
    for h in list_4:
        if h[0:2] != "__":
            print("{}".format(h))
