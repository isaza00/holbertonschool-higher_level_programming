#!/usr/bin/python3
""" Base module contains class Base """


class Base():
    """ base clase for checking id for other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
