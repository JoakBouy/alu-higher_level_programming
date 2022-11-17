#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """
    mylist inheriting from list
    """
    def print_sorted(self):
        print(sorted(self))
