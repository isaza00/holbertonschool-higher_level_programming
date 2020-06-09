#!/usr/bin/python3
""" unit test for square class """


import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ test class for Square class """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ 10 check if square is instance of Base and Rect """
        s = Square(1)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_number_arguments(self):
        """ 10 check if number of arg is right """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)

    def test_correct_arguments(self):
        with self.assertRaises(TypeError):
            s = Square(1, x=3, y=4, i=5)
        with self.assertRaises(TypeError):
            s = Square(1, x=3, e=4, id=5)
        with self.assertRaises(TypeError):
            s = Square(1, g=3, y=4, id=5)

    """ TEST ID CONTINUITY """

    def test_continues_id1(self):
        """ 10 check if the id is continuous """
        s1 = Square(2, 3, 4)
        s2 = Square(2, 3, 4)
        s3 = Square(2, 3, 4, id=100)
        s4 = Square(2, 3, 4)
        s5 = Square(2, 3, 4, 101)
        s6 = Square(2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 100)
        self.assertEqual(s4.id, 3)
        self.assertEqual(s5.id, 101)
        self.assertEqual(s6.id, 4)

    def test_continues_id2(self):
        """ 10 check if the id is continuous """
        s1 = Square(2, 3, 4, 100)
        s2 = Square(2, 3, 4)
        s3 = Square(2, 3, 4)
        s4 = Square(2, 3, 4)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s3.id, 2)
        self.assertEqual(s4.id, 3)

    def test_continues_id3(self):
        """ 10 check if the id is continuous """
        """
        s1 = Square(10)
        s2 = Square(10, id=3)
        s3 = Square(10)
        s4 = Square(10)
        s5 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 3)
        self.assertEqual(s3.id, 2)
        self.assertEqual(s4.id, 4)
        self.assertEqual(s5.id, 5)
        """
        pass

    """ TEST FOR __STR__ METHOD """

    def test_printing(self):
        """ 10 check overloading of __str__ """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 5, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 5/1 - 5")
        s3 = Square(1, 2)
        self.assertEqual(s3.__str__(), "[Square] (2) 2/0 - 1")
        output = io.StringIO()
        sys.stdout = output
        s1 = Square(4, 2, 1, 12)
        print(s1)
        self.assertEqual(output.getvalue(), "[Square] (12) 2/1 - 4\n")
        sys.stdout = sys.__stdout__

    """ GETTER METHOD FOR SIZE """

    def test_getter_method_size(self):
        """ check getter width """
        s = Square(20)
        self.assertEqual(s.size, 20)

    """ TEST SETTER METHODS """

    def test_setter_method_size(self):
        """ check setter method """
        s = Square(1)
        s.size = 3
        self.assertEqual(s.size, 3)

    """ TESTS FOR TYPE ERROR NOT IN VALIDATION WIDTH AND HEIGHT """
    def test_validate_int_width(self):
        """ 10 test int and >= 0 """
        msg_width = "width must be an integer"

        """ test string """
        with self.assertRaises(TypeError) as e:
            s = Square("a")
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = "a"
        self.assertEqual(msg_width, str(e.exception))

        """ test tuple """
        with self.assertRaises(TypeError) as e:
            s = Square((1,))
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = (1,)
        self.assertEqual(msg_width, str(e.exception))

        """ test list """
        with self.assertRaises(TypeError) as e:
            s = Square([1])
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = [1]
        self.assertEqual(msg_width, str(e.exception))

        """ test dict """
        with self.assertRaises(TypeError) as e:
            s = Square({"a": 1})
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = {"a": 1}
        self.assertEqual(msg_width, str(e.exception))

        """ test set """
        with self.assertRaises(TypeError) as e:
            s = Square({"a", "b"})
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = {"a", "b"}
        self.assertEqual(msg_width, str(e.exception))

        """ test float """
        with self.assertRaises(TypeError) as e:
            s = Square(2.75)
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = 2.75
        self.assertEqual(msg_width, str(e.exception))

        """ test Bool """
        with self.assertRaises(TypeError) as e:
            s = Square(True)
        self.assertEqual(msg_width, str(e.exception))

        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = False
        self.assertEqual(msg_width, str(e.exception))

    """ TESTS FOR VALUE VALIDATION <= 0 FOR SIZE AND HEIGHT"""
    def test_validate_positive_size(self):
        """ 10 test error when size <= 0 """
        msg_width = "width must be > 0"
        with self.assertRaises(ValueError) as e:
            s = Square(0)
        self.assertEqual(msg_width, str(e.exception))
        s = Square(1)
        with self.assertRaises(ValueError) as e:
            s.size = 0
        self.assertEqual(msg_width, str(e.exception))
        s = Square(1)
        with self.assertRaises(ValueError) as e:
            s = Square(-1)
        self.assertEqual(msg_width, str(e.exception))
        s = Square(1)
        with self.assertRaises(ValueError) as e:
            s.size = -1
        self.assertEqual(msg_width, str(e.exception))

    """ TEST FOR DISPLAY() METHOD """
    def test_display(self):
        """ 10 test for display method """
        output = io.StringIO()
        sys.stdout = output
        s = Square(3)
        s.display()
        self.assertEqual(output.getvalue(), "###\n###\n###\n")
        with self.assertRaises(TypeError):
            s.display(2)
        with self.assertRaises(TypeError):
            s.display(2, 3)
        s = Square(1, 4)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), "    #\n")

        s = Square(2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

        s = Square(2, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), " ##\n ##\n")
        sys.stdout = sys.__stdout__

    """ TEST FOR AREA() METHOD """
    def test_area(self):
        """ 10 test for area method """
        s = Square(3)
        self.assertEqual(s.area(), 9)
        with self.assertRaises(TypeError):
            s.area(2)
        with self.assertRaises(TypeError):
            s.area(2, 3)

    """ TEST FOR UPDATE WITH ARGS AND KWARGS """

    def test_update_args_kwargs(self):
        """ 12 test for args and kwars on update method """
        s = Square(10, 10, 10)
        s.update(1, y=2, x=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.size, 10)
        s.update(1, size=3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.id, 1)
        s = Square(1, 2, 3, 4)
        dic = {"size": 30, "x": 40, "y": 50, "id": 60}
        s.update(1, 2, 3, 4, dic)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        s.update(**dic)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)
        self.assertEqual(s.id, 60)
        lis = (1, 2, 3, 4)
        s.update(*lis, **dic)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        s.update(**dic)
        self.assertEqual(s.id, 60)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)
        s.update(y=1, size=2, x=3, id=5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)
        s.update(size=10)
        s.update(x=10)
        s.update(y=10)
        s.update(id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

    """ DICT REPRESENTATION OF A SQUARE CLASS """
    def test_dict_repr(self):
        """ 14 test dict representation of square """
        dic = {"size": 1, "x": 2, "y": 3, "id": 4}
        s = Square(1, 2, 3, 4)
        s_dict = s.to_dictionary()
        self.assertEqual(type(s_dict), dict)
        self.assertEqual(s_dict, dic)

        dic = {"id": 1, "size": 2, "x": 0, "y": 0}
        s1 = Square(2)
        s_dict = s1.to_dictionary()
        self.assertEqual(type(s_dict), dict)
        self.assertEqual(s_dict, dic)

    """ TEST TO_JSON_STRING STATIC METHOD """

    def test_to_json_string(self):
        """ 15 check static method to_json_string Square"""
        s1 = Square(1, 2, 3)
        s2 = Square(10)
        with self.assertRaises(TypeError):
            Square.to_json_string(1)
        lis = [s1.to_dictionary(), s2.to_dictionary()]
        dic1 = '{"id": 1, "size": 1, "x": 2, "y": 3}'
        dic2 = '{"id": 2, "size": 10, "x": 0, "y": 0}'
        string = '[' + dic1 + ', ' + dic2 + ']'
        b_json_dict_str = Rectangle.to_json_string(lis)
        self.assertNotEqual(type(b_json_dict_str), dict)
        self.assertEqual(type(b_json_dict_str), str)
        self.assertEqual(b_json_dict_str, string)

    """ TEST TO SAVE_TO_FILE CLASS METHOD """

    def test_save_to_file(self):
        """ 16 check class method to save_to_file Square """
        s1 = Square(2, 3, 4, 5)
        s2 = Square(7, 8, 9, 10)

        lis = [s1, s2]
        l_dic = [obj.to_dictionary() for obj in lis]
        result = Square.to_json_string(l_dic)
        Square.save_to_file(lis)
        with open("Square.json", mode="r", encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, result)

        test = Square(1)
        Square.save_to_file([test])
        testText = Square.to_json_string([test.to_dictionary()])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), testText)

    """ TEST FROM JSON STRING TO DICT """

    def test_from_json_string(self):
        """17 test for from json string to dict Rectangle """
        str1 = 1
        str2 = (1,)
        str3 = {1, 2}
        str4 = {"a": 1}
        str5 = True
        str6 = 1.45
        with self.assertRaises(TypeError):
            Square.from_json_string(str1)
        with self.assertRaises(TypeError):
            Square.from_json_string(str2)
        with self.assertRaises(TypeError):
            Square.from_json_string(str3)
        with self.assertRaises(TypeError):
            Square.from_json_string(str4)
        with self.assertRaises(TypeError):
            Square.from_json_string(str5)
        with self.assertRaises(TypeError):
            Square.from_json_string(str6)
        str1 = None
        str2 = "[]"
        str3 = ""
        lis = Square.from_json_string(str1)
        self.assertEqual(lis, [])
        lis = Square.from_json_string(str2)
        self.assertEqual(lis, [])
        lis = Square.from_json_string(str3)
        self.assertEqual(lis, [])

        s = Square(1)
        s.update(10, 10, 10, 10)
        str3 = s.to_dictionary()
        json_str = Square.to_json_string([str3])
        lis = Square.from_json_string(json_str)
        self.assertEqual(type(lis), list)
        self.assertEqual(lis, [str3])

    """ TEST TO CREATE AN INSTANCE WITH ALL ATTRIBUTES AS DICT """

    def test_create(self):
        """ 18 returns an instance with all attrs set Square """
        dic = {'id': 1, 'size': 3, 'x': 4, 'y': 5}
        s = Square.create(**dic)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, dic)

        str4 = {}
        dic = {'id': 2, 'size': 1, 'x': 0, 'y': 0}
        s = Square.create(**str4)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, dic)

        dic = {'id': 3, 'size': 20, 'x': 0, 'y': 0}
        s = Square.create(size=20)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, dic)

        with self.assertRaises(TypeError):
            s = Square.create(1, 2)

    """ TEST TO LOAD FROM FILE """

    def test_load_from_file(self):
        """ return a list of instances from a file Square """
        a = "Square.json"
        if os.path.exists(a):
            os.remove(a)
        lis = Square.load_from_file()
        self.assertEqual(lis, [])

        s1 = Square(1, 2, 3, 4)
        s2 = Square(6, 7, 8, 9)
        s1_d = s1.to_dictionary()
        s2_d = s2.to_dictionary()
        Square.save_to_file([s1, s2])
        lis = Square.load_from_file()
        s1_s = lis[0].to_dictionary()
        s2_s = lis[1].to_dictionary()
        self.assertEqual(s1_s, s1_d)
        self.assertEqual(s2_s, s2_d)
