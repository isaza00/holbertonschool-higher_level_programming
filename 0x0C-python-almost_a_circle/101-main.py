#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(20, 50, 20, 30), Rectangle(30, 40, 10, 10), Rectangle(10, 10, 10, 10)]
    list_squares = [Square(20, 30, 30), Square(40, 10, 15), Square(10, 10, 10)]

    Base.draw(list_rectangles, list_squares)