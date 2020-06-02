#!/usr/bin/python3
"""
    class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by
        integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the
    square description: [Square] <width>/<height>
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square inherits from rectangle class """

    def __init__(self, size):
        """ initializes square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return super().area()

    def __str__(self):
        """ returns [Square] <width>/<height> string """
        a = str(self.__size)
        return "[Square] " + a + "/" + a
