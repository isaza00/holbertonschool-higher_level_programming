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
        res = (mult / sum)
    return (truncate(res, 2))

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
