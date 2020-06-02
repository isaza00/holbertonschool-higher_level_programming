#!/usr/bin/python3
""" returs a list of available attributes and methods """


def lookup(obj):
    """ look for all attributes and methods of obj """
    return [method for method in dir(obj)]
