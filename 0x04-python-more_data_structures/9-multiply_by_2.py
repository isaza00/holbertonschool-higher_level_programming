#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    if a_dictionary:
        for x in a_dictionary:
            new_d[x] = a_dictionary[x] * 2
    return (new_d)
