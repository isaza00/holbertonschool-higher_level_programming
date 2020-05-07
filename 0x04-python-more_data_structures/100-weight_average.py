#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    res = 0
    mult = 0
    sum = 0
    for i in my_list:
        mult += i[0] * i[1]
        sum += i[1]
        if sum == 0:
            return 0
        res = int((mult / sum)*20) / 20
    return (res)
