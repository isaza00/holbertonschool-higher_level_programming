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
        return (self._size * self._size)

    @property
    def size(self):
        """The summary line for a class docstring should fit on one line."""
        return self._size

    @property
    def position(self):
        """The summary line for a class docstring should fit on one line."""
        return self._position

    @size.setter
    def size(self, value):
        """The summary line for a class docstring should fit on one line."""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """The summary line for a class docstring should fit on one line."""
        if (type(value) == tuple and len(value) == 2 and
                type(value[0]) == int and type(value[1]) == int):
                self._position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """The summary line for a class docstring should fit on one line."""
        i, j = 0, 0
        x, y = 0, 0
        if self._size == 0:
            print()
        else:
            while y < self._position[1]:
                print()
                y += 1
            while i < self._size:
                while x < self._position[0]:
                    print(" ", end="")
                    x += 1
                while j < self._size:
                    print("#", end="")
                    j += 1
                print()
                x = 0
                j = 0
                i += 1
