#!/usr/bin/python3
""" Unit tests for base module """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ tests cases for base clase """

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

    def test_no_repetition(self):
        """ check if the id is continuous """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(3)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        with self.assertRaises(ValueError):
            self.assertEqual(b4.id, 3)
        
    
    def test_number_arguments(self):
        """ check if it has right amount of args """
        with self.assertRaises(TypeError):
            b = Base(1, 2)
    
    def test_private_class_var(self):
        """ check if private var nb_object is private """
        with self.assertRaises(AttributeError):
            Base.__nb_objects
