#!/usr/bin/python3


"""Example Google style docstrings."""


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0):
        """The summary line for a class docstring should fit on one line."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self._size = size
