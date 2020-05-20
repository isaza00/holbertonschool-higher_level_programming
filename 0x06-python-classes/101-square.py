#!/usr/bin/python3


"""The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.

    """


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0, position=(0, 0)):
        """The summary line for a class docstring should fit on one line."""
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """The summary line for a class docstring should fit on one line."""
        str = "position must be a tuple of 2 positive integers"
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
                raise TypeError(str)
        else:
            self.__position = value

    def area(self):
        """The summary line for a class docstring should fit on one line."""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                if i != self.__size - 1:
                    print()
        return ""

    def __str__(self):
        return str(self.my_print())
