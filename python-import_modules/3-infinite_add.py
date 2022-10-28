#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    all = 0
    for number in range(1, len(sys.argv)):
        all += int(sys.argv[number])
    print("{}".format(all))
