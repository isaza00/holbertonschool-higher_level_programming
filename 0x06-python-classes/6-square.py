#!/usr/bin/python3


"""Example Google style docstrings."""


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0, position=(0, 0)):
        """The summary line for a class docstring should fit on one line."""
        self.size = size
        self.position = position

    def area(self):
        """The summary line for a class docstring should fit on one line."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """The summary line for a class docstring should fit on one line."""
        return self.__size

    @property
    def position(self):
        """The summary line for a class docstring should fit on one line."""
        return self.__position

    @size.setter
    def size(self, value):
        """The summary line for a class docstring should fit on one line."""
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """The summary line for a class docstring should fit on one line."""
        if (type(value) == tuple and len(value) == 2 and
                type(value[0]) == int and type(value[1]) == int):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """The summary line for a class docstring should fit on one line."""
        i, y = 0, 0
        if self.__size is 0:
            print()
        else:
            while y < self.__position[1]:
                print()
                y += 1
            while i < self.__size:
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
                i += 1
