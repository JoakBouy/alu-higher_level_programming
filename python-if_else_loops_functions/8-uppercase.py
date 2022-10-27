#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= 123 and ord(i) >= 97:
            upper = chr(ord(i) - 32)
            i = upper
        print("{}".format(i), end='')
    print()
