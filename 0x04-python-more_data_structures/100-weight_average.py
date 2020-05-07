#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mult = 1
        sum = 0
        for i in my_list:
            mult += i[0] * i[1]
            sum += i[1]
            res = int((mult / sum) * 10) / 10
        return (res)
    else:
        return 0
