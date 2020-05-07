#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mult = 0
        sum = 0
        for i in my_list:
            mult += i[0] * i[1]
            sum += i[1]
        return (mult / sum)
    else:
        return (0)
