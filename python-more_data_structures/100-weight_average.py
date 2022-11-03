#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0.0
    s_list = list(i[0] * i[1] for i in my_list)
    w_list = list(i[1] for i in my_list)
    res = sum(s_list) / sum(w_list)
    return res
