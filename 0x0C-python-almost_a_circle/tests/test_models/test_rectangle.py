#!/usr/bin/python3
""" unit test for rectangle class """


import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ class test for testing rectangle class """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ check if rectangle is instance of Base and Rect """
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def test_number_arguments(self):
        """ check if number of arg is right """
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_correct_arguments(self):
        """ test correct arguments """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, y=4, i=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, e=4, id=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, g=3, y=4, id=5)

    def test_continues_id1(self):
        """ check if the id is continuous """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2, 3, 4, id=100)
        r4 = Rectangle(1, 2, 3, 4)
        r5 = Rectangle(1, 2, 3, 4, 101)
        r6 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 100)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r5.id, 101)
        self.assertEqual(r6.id, 4)

    def test_continues_id2(self):
        """ check if the id is continuous """
        r1 = Rectangle(1, 2, 3, 4, 100)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r4.id, 3)

    def test_private_width(self):
        """ check if private var width is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_private_height(self):
        """ check if private var height is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__height

    def test_private_x(self):
        """ check if private var x is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__x

    def test_private_y(self):
        """ check if private var y is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__y

    def test_getter_method_width(self):
        """ check getter width """
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)

    def test_getter_method_height(self):
        """ check getter height """
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_getter_method_x(self):
        """ check getter x """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, x=4)
        self.assertEqual(r.x, 4)

    def test_getter_method_y(self):
        """ check getter y """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r = Rectangle(1, 2, 3, y=5)
        self.assertEqual(r.y, 5)

    def test_setter_method_width(self):
        """ check setter method width """
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)

    def test_setter_method_height(self):
        """ check setter method height """
        r = Rectangle(1, 2)
        r.height = 3
        self.assertEqual(r.height, 3)

    def test_setter_method_x(self):
        """ check setter method x"""
        r = Rectangle(1, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, x=3)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_setter_method_y(self):
        """ check setter method y"""
        r = Rectangle(1, 2)
        r.y = 3
        self.assertEqual(r.y, 3)
        r = Rectangle(1, 2, y=3)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_validate_int_width(self):
        """ test int and >= 0 """
        msg_width = "width must be an integer"
        """ test string """
        with self.assertRaises(TypeError) as e:
            r = Rectangle("a", 1)
        self.assertEqual(msg_width, str(e.exception))
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            r.width = "a"
        self.assertEqual(msg_width, str(e.exception))
        """ test tuple """
        with self.assertRaises(TypeError) as e:
            r = Rectangle((1,), 2)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = (1,)
        self.assertEqual(msg_width, str(e.exception))
        """ test list """
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1], 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = [1]
        self.assertEqual(msg_width, str(e.exception))
        """ test dict """
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"a": 1}, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = {"a": 1}
        self.assertEqual(msg_width, str(e.exception))
        """ test set """
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"a", "b"}, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = {"a", "b"}
        self.assertEqual(msg_width, str(e.exception))
        """ test float """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2.75, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = 2.75
        self.assertEqual(msg_width, str(e.exception))
        """ test Bool """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(True, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.width = False
        self.assertEqual(msg_width, str(e.exception))

    def test_validate_int_height(self):
        """ test int and >= 0 """
        msg_height = "height must be an integer"
        """ test string """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "a")
        self.assertEqual(msg_height, str(e.exception))
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            r.height = "a"
        self.assertEqual(msg_height, str(e.exception))
        """ test tuple """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2, (1,))
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = (1,)
        self.assertEqual(msg_height, str(e.exception))
        """ test list """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, [1])
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = [1]
        self.assertEqual(msg_height, str(e.exception))
        """ test dict """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, {"a": 1})
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = {"a": 1}
        self.assertEqual(msg_height, str(e.exception))
        """ test set """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, {"a", "b"})
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = {"a", "b"}
        self.assertEqual(msg_height, str(e.exception))
        """ test float """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2.75)
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = 2.75
        self.assertEqual(msg_height, str(e.exception))
        """ test Bool """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, True)
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.height = False
        self.assertEqual(msg_height, str(e.exception))

    def test_validate_int_x(self):
        """ test int and >= 0 """
        msg_x = "x must be an integer"
        """ test string """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, "a", 1)
        self.assertEqual(msg_x, str(e.exception))
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            r.x = "a"
        self.assertEqual(msg_x, str(e.exception))
        """ test tuple """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, (1,), 2)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = (1,)
        self.assertEqual(msg_x, str(e.exception))
        """ test list """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, [1], 1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = [1]
        self.assertEqual(msg_x, str(e.exception))
        """ test dict """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, {"a": 1}, 1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = {"a": 1}
        self.assertEqual(msg_x, str(e.exception))
        """ test set """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, {"a", "b"}, 1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = {"a", "b"}
        self.assertEqual(msg_x, str(e.exception))
        """ test float """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 2.75, 1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = 2.75
        self.assertEqual(msg_x, str(e.exception))
        """ test Bool """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, True, 1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.x = False
        self.assertEqual(msg_x, str(e.exception))

    def test_validate_int_y(self):
        """ test int and >= 0 """
        msg_y = "y must be an integer"
        """ test string """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, "a")
        self.assertEqual(msg_y, str(e.exception))
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            r.y = "a"
        self.assertEqual(msg_y, str(e.exception))
        """ test tuple """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, (1,))
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = (1,)
        self.assertEqual(msg_y, str(e.exception))
        """ test list """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, [1])
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = [1]
        self.assertEqual(msg_y, str(e.exception))
        """ test dict """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, {"a": 1})
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = {"a": 1}
        self.assertEqual(msg_y, str(e.exception))
        """ test set """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, {"a", "b"})
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = {"a", "b"}
        self.assertEqual(msg_y, str(e.exception))
        """ test float """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, 2.75)
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = 2.75
        self.assertEqual(msg_y, str(e.exception))
        """ test Bool """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, True)
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.y = False
        self.assertEqual(msg_y, str(e.exception))

    def test_validate_positive_width(self):
        """ test error when width <= 0 """
        msg_width = "width must be > 0"
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2)
            r.width = 0
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 1)
        self.assertEqual(msg_width, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2)
            r.width = -1
        self.assertEqual(msg_width, str(e.exception))

    def test_validate_positive_height(self):
        """ test error when height <= 0 """
        msg_height = "height must be > 0"
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2)
            r.height = 0
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -1)
        self.assertEqual(msg_height, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2)
            r.height = -1
        self.assertEqual(msg_height, str(e.exception))

    def test_validate_positive_x(self):
        """ test error when x < 0 """
        msg_x = "x must be >= 0"
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, x=-1)
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2)
            r.x = -1
        self.assertEqual(msg_x, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3)
            r.x = -1
        self.assertEqual(msg_x, str(e.exception))

    def test_validate_positive_y(self):
        """ test error when y < 0 """
        msg_y = "y must be >= 0"
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -1)
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, y=-1)
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3)
            r.y = -1
        self.assertEqual(msg_y, str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4)
            r.y = -1
        self.assertEqual(msg_y, str(e.exception))

    def test_area(self):
        """ 4 test for area method """
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        with self.assertRaises(TypeError):
            r.area(2)
        with self.assertRaises(TypeError):
            r.area(2, 3)

    def test_display(self):
        """ 5 and 7 test for display method """
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(4, 3)
        r.display()
        self.assertEqual(output.getvalue(), "####\n####\n####\n")
        with self.assertRaises(TypeError):
            r.display(2)
        with self.assertRaises(TypeError):
            r.display(2, 3)
        r = Rectangle(1, 4)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), "#\n#\n#\n#\n")
        r = Rectangle(2, 3, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        r = Rectangle(3, 2, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), " ###\n ###\n")
        sys.stdout = sys.__stdout__

    def test_printing(self):
        """ 6 override __str method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        r3 = Rectangle(1, 2)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 0/0 - 1/2")
        output = io.StringIO()
        sys.stdout = output
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
        r2 = Rectangle(5, 5, 1)
        output = io.StringIO()
        sys.stdout = output
        print(r2)
        self.assertEqual(output.getvalue(), "[Rectangle] (3) 1/0 - 5/5\n")
        r3 = Rectangle(1, 2)
        output = io.StringIO()
        sys.stdout = output
        print(r3)
        self.assertEqual(output.getvalue(), "[Rectangle] (4) 0/0 - 1/2\n")
        sys.stdout = sys.__stdout__

    def test_update(self):
        """ 8 test for update method """
        r = Rectangle(10, 20, 30, 40, 50)
        r.update()
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        r.update(89, 90, 91)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 90)
        self.assertEqual(r.height, 91)
        r.update(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        r.update(89, 90, 91, 92, 93)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 90)
        self.assertEqual(r.height, 91)
        self.assertEqual(r.x, 92)
        self.assertEqual(r.y, 93)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = ()
        r.update(*lis)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = (1, 2)
        r.update(*lis)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = (10, 20, 30, 40, 50)
        r.update(*lis)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        lis = (10, -20, 30, 40, 50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 20, -30, 40, 50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 20, 30, -40, 50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 20, 30, 40, -50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 0, 30, 40, 50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 20, 0, 40, 50)
        with self.assertRaises(ValueError):
            r.update(*lis)
        lis = (10, 20, 30, 40, "a")
        with self.assertRaises(TypeError):
            r.update(*lis)
        lis = (10, "a", 30, 40, 50)
        with self.assertRaises(TypeError):
            r.update(*lis)
        lis = (10, 20, "a", 40, 50)
        with self.assertRaises(TypeError):
            r.update(*lis)
        lis = (10, 20, 30, "a", 50)
        with self.assertRaises(TypeError):
            r.update(*lis)

    def test_update_args_kwargs(self):
        """8 and 9 test for args and kwars on update method Rectangle"""
        r = Rectangle(10, 10, 10, 10)
        r.update(100, height=2, x=3)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.width, 10)
        r.update(1, 1, 2, width=3, height=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        r = Rectangle(10, 20, 30, 40, 50)
        dic = {"width": 20, "height": 30, "x": 40, "y": 50, "id": 60}
        r.update(1, 2, 3, 4, 5, dic)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(**dic)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        self.assertEqual(r.id, 60)
        lis = [1, 2, 3, 4, 5]
        r.update(*lis, **dic)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(**dic)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        r.update(y=1, width=2, x=3, height=4, id=5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)
        r.update(width=10)
        r.update(height=10)
        r.update(x=10)
        r.update(y=10)
        r.update(id=10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        r.update(a=5, b=2, i=3, width=1, height=2, x=3, y=4, id=6)

    def test_dict_repr(self):
        """ 13 test dict representation of rectangle Rect """
        dic = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, dic)
        self.assertEqual(type(r_dict), dict)

        dic = {"width": 1, "height": 2, "x": 0, "y": 0, "id": 1}
        r1 = Rectangle(1, 2)
        r_dict = r1.to_dictionary()
        self.assertEqual(type(r_dict), dict)
        self.assertEqual(r_dict, dic)

    def test_save_to_file(self):
        """ 16 check class method to save_to_file Rectange """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)

        lis = [r1, r2]
        l_dic = [obj.to_dictionary() for obj in lis]
        result = Rectangle.to_json_string(l_dic)
        Rectangle.save_to_file(lis)
        with open("Rectangle.json", mode="r", encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, result)

        test = Rectangle(1, 2)
        Rectangle.save_to_file([test])
        testText = Rectangle.to_json_string([test.to_dictionary()])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), testText)

    def test_from_json_string(self):
        """17 test for from json string to dict Rectangle """
        str1 = 1
        str2 = (1,)
        str3 = {1, 2}
        str4 = {"a": 1}
        str5 = True
        str6 = 1.45
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str1)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str2)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str3)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str4)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str5)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(str6)
        str1 = None
        str2 = "[]"
        str3 = ""
        lis = Rectangle.from_json_string(str1)
        self.assertEqual(lis, [])
        lis = Rectangle.from_json_string(str2)
        self.assertEqual(lis, [])
        lis = Rectangle.from_json_string(str3)
        self.assertEqual(lis, [])

        r = Rectangle(1, 2)
        r.update(10, 10, 10, 10, 10)
        str3 = r.to_dictionary()
        json_str = Rectangle.to_json_string([str3])
        lis = Rectangle.from_json_string(json_str)
        self.assertEqual(type(lis), list)
        self.assertEqual(lis, [str3])

    def test_create(self):
        """ 18 returns an instance with all attrs set Rect"""
        dic = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        r = Rectangle.create(**dic)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, dic)

        str4 = {}
        dic = {'id': 2, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        r = Rectangle.create(**str4)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, dic)

        dic = {'id': 3, 'width': 20, 'height': 1, 'x': 0, 'y': 0}
        r = Rectangle.create(width=20)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, dic)

        with self.assertRaises(TypeError):
            r = Rectangle.create(1, 2)

    def test_load_from_file(self):
        """ return a list of instances from a file """
        a = "Rectangle.json"
        if os.path.exists(a):
            os.remove(a)
        lis = Rectangle.load_from_file()
        self.assertEqual(lis, [])

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        r1_d = r1.to_dictionary()
        r2_d = r2.to_dictionary()
        Rectangle.save_to_file([r1, r2])
        lis = Rectangle.load_from_file()
        r1_s = lis[0].to_dictionary()
        r2_s = lis[1].to_dictionary()
        self.assertEqual(r1_s, r1_d)
        self.assertEqual(r2_s, r2_d)

    def test_save_to_file_csv(self):
        """ 20 check class method to save_to_file CVS Rectange """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        lis1 = "a"
        lis2 = {r1, r2}
        lis3 = {'b1': 1, 'b2': 2}
        lis3 = (r1, r2)
        lis4 = 1.55
        lis5 = r1
        lis6 = 1
        lis = [r1, 2]
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis1)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis2)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis4)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis5)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis6)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(lis)

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        b = 5
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([r1, b])

        lis = [r1, r2]
        result = "5,1,2,3,4\n10,6,7,8,9\n"

        Rectangle.save_to_file_csv(lis)
        with open("Rectangle.csv", mode="r", encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, result)

        test = Rectangle(1, 2)
        result = "3,1,2,0,0\n"
        Rectangle.save_to_file_csv([test])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), result)
