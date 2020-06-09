#!/usr/bin/python3
""" rectangle module contains class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ rectangle clase for rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init with arguments and __init__ from Base """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints the rectangle using # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ change str representantion when print object """
        id_str = str(self.id)
        w_str = str(self.__width)
        h_str = str(self.__height)
        x_str = str(self.__x)
        y_str = str(self.__y)
        div_str = x_str + '/' + y_str + ' - ' + w_str + '/' + h_str
        return ("[Rectangle] " + '(' + id_str + ') ' + div_str)

    def update(self, *args, **kwargs):
        """ update id, width, height, x and y, this order """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ 13 return dict representation of a rectangle """
        i = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        dic = {'id': i, 'width': w, 'height': h, 'x': x, 'y': y}
        return dic
