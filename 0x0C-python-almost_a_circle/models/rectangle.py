#!/usr/bin/python3
""" rectangle module contains class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ rectangle clase for rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init with arguments and __init__ from Base """
        pass

r = Rectangle(1, 1)
print(r)