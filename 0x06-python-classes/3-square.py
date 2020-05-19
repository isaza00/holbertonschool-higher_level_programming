#!/usr/bin/python3


"""Example Google style docstrings."""


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0):
        """The summary line for a class docstring should fit on one line."""
        if type(size) == int:
            if size >= 0:
                self._size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """The summary line for a class docstring should fit on one line."""
        return (self._size * self._size)
