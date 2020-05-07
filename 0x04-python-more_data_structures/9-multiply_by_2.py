#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        for x in a_dictionary:
            a_dictionary[x] *= 2
    return (a_dictionary)
