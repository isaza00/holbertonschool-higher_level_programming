#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)

    Instantiation with width and height: def
    __init__(self, width, height)::
        width and height must be private.
        No getter or setter
        width and height must be positive
        integers validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return,
    the following rectangle description:
    [Rectangle] <width>/<height>
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

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns [Rectangle] <width>/<height> string """
        a = str(self.__width)
        b = str(self.__height)
        return "[" + __class__.__name__ + "] " \
            + a + "/" + b
