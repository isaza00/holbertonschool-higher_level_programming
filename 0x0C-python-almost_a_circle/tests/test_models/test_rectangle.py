#!/usr/bin/python3
""" unit test for rectangle class """


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ class test for testing rectangle class """

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
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, y=4, i=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, e=4, id=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, g=3, y=4, id=5)

    """ TEST ID CONTINUITY """

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
        r1 = Rectangle(100)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r4.id, 3)

    """ TEST PRIVATE VARIABLES """

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

    """ GETTER METHODS """

    def test_getter_method_width(self):
        """ check getter width """
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)

    def test_getter_method_height(self):
        """ check getter width """
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_getter_method_x(self):
        """ check getter width """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, 3, x=4)
        self.assertEqual(r.x, 4)

    def test_getter_method_y(self):
        """ check getter width """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r = Rectangle(1, 2, 3, 4, y=5)
        self.assertEqual(r.y, 5)

    """ TEST SETTER METHODS """

    def test_setter_method_width(self):
        """ check setter method """
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)
    
    def test_setter_method_height(self):
        """ check setter method """
        r = Rectangle(1, 2)
        r.height = 3
        self.assertEqual(r.height, 3)
    
    def test_setter_method_x(self):
        """ check setter method """
        r = Rectangle(1, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, x=3)
        r.x = 4
        self.assertEqual(r.x, 4)
    
    def test_setter_method_y(self):
        """ check setter method """
        r = Rectangle(1, 2)
        r.y = 3
        self.assertEqual(r.y, 3)
        r = Rectangle(1, 2, y=3)
        r.y = 4
        self.assertEqual(r.y, 4)

    """ TESTS FOR TYPE ERROR NOT IN VALIDATION WIDTH AND HEIGHT """

    def test_validate_int_width(self):
        """ test int and >= 0 """
        msg_width = "width must be an integer"
        """ test string """
        try:
            r = Rectangle("a", 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = "a"
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test tuple """
        try:
            r = Rectangle((1,), 2)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = (1,)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test list """
        try:
            r = Rectangle([1], 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = [1]
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test dict """
        try:
            r = Rectangle({"a": 1}, 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = {"a": 1}
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test set """
        try:
            r = Rectangle({"a", "b"}, 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = {"a", "b"}
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test float """
        try:
            r = Rectangle(2.75, 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = 2.75
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        """ test Bool """
        try:
            r = Rectangle(True, 1)
        except TypeError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = False
        except TypeError as e:
            self.assertEqual(e.message, msg_width)

    def test_validate_int_height(self):
        """ test int and >= 0 """
        msg_height = "height must be an integer"
        """ test string """
        try:
            r = Rectangle(1, "a")
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = "a"
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test tuple """
        try:
            r = Rectangle(2, (1,))
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = (1,)
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test list """
        try:
            r = Rectangle(1, [1])
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = [1]
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test dict """
        try:
            r = Rectangle(1, {"a": 1})
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = {"a": 1}
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test set """
        try:
            r = Rectangle(1, {"a", "b"})
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = {"a", "b"}
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test float """
        try:
            r = Rectangle(1, 2.75)
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = 2.75
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        """ test Bool """
        try:
            r = Rectangle(1, True)
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = False
        except TypeError as e:
            self.assertEqual(e.message, msg_height)
        
    """ TESTS FOR VALUE VALIDATION <= 0 FOR WIDTH AND HEIGHT"""

    def test_validate_positive_width(self):
        """ test error when width <= 0 """
        msg_width = "width must be > 0"
        try:
            r = Rectangle(0, 1)
        except ValueError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = 0
        except ValueError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(-1, 1)
        except ValueError as e:
            self.assertEqual(e.message, msg_width)
        try:
            r = Rectangle(1, 2)
            r.width = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_width)

    def test_validate_positive_height(self):
        """ test error when height <= 0 """
        msg_height = "height must be > 0"
        try:
            r = Rectangle(1, 0)
        except ValueError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = 0
        except ValueError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, -1)
        except ValueError as e:
            self.assertEqual(e.message, msg_height)
        try:
            r = Rectangle(1, 2)
            r.height = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_height)

    """ TESTS FOR VALUE VALIDATION < 0 FOR X AND Y"""

    def test_validate_positive_x(self):
        """ test error when x <= 0 """
        msg_x = "x must be >= 0"
        try:
            r = Rectangle(1, 2, -1)
        except ValueError as e:
            self.assertEqual(e.message, msg_x)
        try:
            r = Rectangle(1, 2, x=-1)
        except ValueError as e:
            self.assertEqual(e.message, msg_x)
        try:
            r = Rectangle(1, 2)
            r.x = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_x)
        try:
            r = Rectangle(1, 2, 3)
            r.x = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_x)
        

    def test_validate_positive_y(self):
        """ test error when y <= 0 """
        msg_y = "y must be >= 0"
        try:
            r = Rectangle(1, 2, 3, -1)
        except ValueError as e:
            self.assertEqual(e.message, msg_y)
        try:
            r = Rectangle(1, 2, y=-1)
        except ValueError as e:
            self.assertEqual(e.message, msg_y)
        try:
            r = Rectangle(1, 2, 3)
            r.y = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_y)
        try:
            r = Rectangle(1, 2, 3, 4)
            r.y = -1
        except ValueError as e:
            self.assertEqual(e.message, msg_y)
    
    """ TEST FOR AREA() METHOD """

    def test_area(self):
        """ test for area method """
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        with self.assertRaises(TypeError):
            r.area(2)
        with self.assertRaises(TypeError):
            r.area(2, 3)

    """ TEST FOR DISPLAY() METHOD """
    
    def test_display(self):
        """ test for display method """
        r = Rectangle(4, 3)
        self.assertEqual(r.display, "####\n####\n####\n")
        with self.assertRaises(TypeError):
            r.display(2)
        with self.assertRaises(TypeError):
            r.display(2, 3)
        r = Rectangle(1, 4)
        self.assertEqual(r.display, "#\n#\n#\n#\n")
        r = Rectangle(3, 3, 2, 2)
        self.assertEqual(r.display, "\n\n  ##\n  ##\n  ##\n")
        r = Rectangle(3, 2, 1, 0)
        self.assertEqual(r.display, " ###\n ###\n")

    """ TEST FOR __STR__ METHOD """

    def test_printing(self):
        """ override __str method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(print(r2), "[Rectangle] (1) 1/0 - 5/5")
        r3 = Rectangle(1, 2)
        self.assertEqual(print(r2), "[Rectangle] (2) 0/0 - 1/2")
    
    """ TEST FOR UPDATE METHOD """

    def test_update(self):
        """ test for update method """
        r = Rectangle(10, 20, 30, 40, 50)
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
        self.assertEqual(r.x, 93)






