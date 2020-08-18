#!/usr/bin/python3
""" find min number of a list """


def find_peak(list_of_integers):
    """ call recursive function """
    if not list_of_integers:
        return
    length = len(list_of_integers)
    return find_recursively(list_of_integers, 0, length - 1, length)


def find_recursively(lista, low, high, length):
    """ find peak recursively """
    mid = (low + high)/2
    mid = int(mid)
    if (mid == 0 or lista[mid - 1] <= lista[mid])\
            and (mid == (length - 1) or lista[mid + 1] <= lista[mid]):
                return lista[mid]
    elif mid > 0 and lista[mid - 1] > lista[mid]:
        return find_recursively(lista, low, mid - 1, length)
    else:
        return find_recursively(lista, mid + 1, high, length)
