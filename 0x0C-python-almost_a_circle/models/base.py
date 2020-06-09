#!/usr/bin/python3
""" Base module contains class Base """


import json
import csv
import turtle


class Base():
    """ base clase for checking id for other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 15 return json str of list of dicts """
        if type(list_dictionaries) != list and list_dictionaries != None:
            raise TypeError
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for dic in list_dictionaries:
            if type(dic) != dict:
                raise TypeError
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string of list_objs to a file """
        if type(list_objs) != list:
            raise TypeError
        for obj in list_objs:
            if not isinstance(obj, cls):
                raise TypeError
        lis = [obj.to_dictionary() for obj in list_objs]
        json_obj = cls.to_json_string(lis)
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """ return python list of json string representation """
        if type(json_string) != str and json_string != None:
            raise TypeError
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a json file"""
        obj_list = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                json_str = f.read()
        except:
            json_str = '[]'
        lis = cls.from_json_string(json_str)
        if lis:
            for dic in lis:
                obj_list.append(cls.create(**dic))
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ return serialize file of list of objects """
        if type(list_objs) != list:
            raise TypeError
        for obj in list_objs:
            if not isinstance(obj, cls):
                raise TypeError
        lis = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        with open(file_name, mode="w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            for dic in lis:
                writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize a csv file into a list """
        obj_list = []
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f, fieldnames=field_names)
                for row in reader:
                    dic = {}
                    for key, value in dict(row).items():
                        dic[key] = int(value)
                    obj_list.append(cls.create(**dic))
        except:
            return []
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ print with turtle list of rectangles and squares """
        turtles = []
        turtles.append(turtle.Turtle())
        #turtle.Screen.title("Welcome to the show")
        pos_x = 0
        pos_y = 0
        for obj in list_rectangles:
            dic = obj.to_dictionary()
            print(dic)
            w = dic['width']
            h = dic['height']
            x = dic['x']
            y = dic['y']
            turtles[0].speed(1)
            turtles[0].color('red')
            turtles[0].pensize(1)
            
            turtles[0].goto(pos_x, 0)

            turtles[0].pendown()
            turtles[0].goto(pos_x + x, -y)
            turtles[0].begin_fill()
            turtles[0].color('blue')
            turtles[0].pensize(5)
            turtles[0].forward(w)
            turtles[0].right(90)
            turtles[0].forward(h)
            turtles[0].right(90)
            turtles[0].forward(w)
            turtles[0].right(90)
            turtles[0].forward(h)
            turtles[0].right(90)
            turtles[0].end_fill()
            turtles[0].penup()
            pos_x += w + 50

        pos_y += -150 - h
        pos_x = 0
        for obj in list_squares:
            dic = obj.to_dictionary()
            print(dic)
            s = dic['size']
            x = dic['x']
            y = dic['y']
            turtles[0].speed(1)
            turtles[0].color('red')
            turtles[0].pensize(1)
            
            turtles[0].goto(pos_x, pos_y)

            turtles[0].pendown()
            turtles[0].goto(pos_x + x, pos_y - y)
            turtles[0].begin_fill()
            turtles[0].color('green')
            turtles[0].pensize(5)
            turtles[0].forward(s)
            turtles[0].right(90)
            turtles[0].forward(s)
            turtles[0].right(90)
            turtles[0].forward(s)
            turtles[0].right(90)
            turtles[0].forward(s)
            turtles[0].right(90)
            turtles[0].end_fill()
            turtles[0].penup()
            pos_x += s + 50

        turtle.Screen().exitonclick()
            
            

