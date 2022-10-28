#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    for a in n:
        if a[0:2] != "__":
            print(a)
