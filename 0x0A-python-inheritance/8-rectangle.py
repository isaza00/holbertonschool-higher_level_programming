#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).

    Instantiation with width and height:
    def __init__(self, width, height):
        width and height must be private.
        No getter or setter
        width and height must be positive integers,
        validated by integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class inherits from basegeometry """

    def __init__(self, width, height):
        """ initialization """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
