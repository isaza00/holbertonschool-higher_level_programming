#!/usr/bin/python3
""" module for locked class """


class LockedClass:
    """ class that just allow attr called first_name """
    __slots__ = ["first_name"]
