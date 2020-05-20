#!/usr/bin/python3
"""MagicClass Module"""
import math


class MagicClass():
    """ Magic class comments """
    def _init_(self, radius=0):
        self.MagicClass_radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.MagicClass_radius = radius

    def area(self):
        return self.MagicClass_radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.MagicClass_radius
