#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for idx in list(a_dictionary.keys()):
        if a_dictionary[idx] == value:
            a_dictionary.pop(idx)

    return a_dictionary
