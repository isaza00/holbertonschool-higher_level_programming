#!/usr/bin/python3
""" Unit tests for base module """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ tests cases for base clase """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ Test if isinstance """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(100)
        self.assertIsInstance(b2, Base)

    def test_continues_id1(self):
        """ check if the id is continuous """
        b1 = Base()
        b2 = Base()
        b3 = Base(100)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 100)
        self.assertEqual(b4.id, 3)

    def test_continues_id2(self):
        """ check if the id is continuous """
        b1 = Base(100)
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_continues_id3(self):
        """ check if the id is continuous """
        """
        b1 = Base()
        b2 = Base(3)
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 5)
        """
        pass

    def test_no_repetition(self):
        """ check if the id is continuous """
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(3)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        with self.assertRaises(ValueError):
            self.assertEqual(b4.id, 3)
        """
        pass

    def test_number_arguments(self):
        """ check if it has right amount of args """
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_private_class_var(self):
        """ check if private var nb_object is private """
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    """ TEST TO_JSON_STRING STATIC METHOD """

    def test_to_json_string(self):
        """ 15 check static method to_json_string BASE """
        b1 = Base()
        b2 = Base()
        lis1 = "a"
        lis2 = {b1, b2}
        lis3 = {'b1': 1, 'b2': 2}
        lis3 = (b1, b2)
        lis4 = 1.55
        lis5 = b1
        lis6 = 1
        lis = [b1.__dict__, b2.__dict__]
        dic = {"id": 1}
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis1)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis2)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis3)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis4)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis5)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string(lis6)
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string()
        with self.assertRaises(TypeError):
            b_json_dict_str = Base.to_json_string([dic], [dic])
        b_json_dict_str = Base.to_json_string([])
        self.assertEqual(b_json_dict_str, "[]")
        b_json_dict_str = Base.to_json_string(None)
        self.assertEqual(b_json_dict_str, "[]")
        b_json_dict_str = Base.to_json_string(lis)
        self.assertNotEqual(type(b_json_dict_str), type(dic))
        self.assertEqual(type(b_json_dict_str), str)
        self.assertEqual(b_json_dict_str, '[{"id": 1}, {"id": 2}]')

    """ TEST TO SAVE_TO_FILE CLASS METHOD """

    def test_save_to_file(self):
        """ 16 check class method to save_to_file Base """
        pass

    """ TEST FROM JSON STRING TO DICT """
    def test_from_json_string(self):
        """17 test for from json string to dict Base """
        str1 = 1
        str2 = (1,)
        str3 = {1, 2}
        str4 = {"a": 1}
        str5 = True
        str6 = 1.45
        with self.assertRaises(TypeError):
            Base.from_json_string(str1)
        with self.assertRaises(TypeError):
            Base.from_json_string(str2)
        with self.assertRaises(TypeError):
            Base.from_json_string(str3)
        with self.assertRaises(TypeError):
            Base.from_json_string(str4)
        with self.assertRaises(TypeError):
            Base.from_json_string(str5)
        with self.assertRaises(TypeError):
            Base.from_json_string(str6)
        str1 = None
        str2 = "[]"
        str3 = ""
        lis = Base.from_json_string(str1)
        self.assertEqual(lis, [])
        lis = Base.from_json_string(str2)
        self.assertEqual(lis, [])
        lis = Base.from_json_string(str3)
        self.assertEqual(lis, [])
        str3 = [{'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        json_str = Base.to_json_string(str3)
        lis = Base.from_json_string(json_str)
        self.assertEqual(type(lis), list)
        self.assertEqual(lis, [{'id': 89, 'width': 10, 'height': 4},
                               {'id': 7, 'width': 1, 'height': 7}])
