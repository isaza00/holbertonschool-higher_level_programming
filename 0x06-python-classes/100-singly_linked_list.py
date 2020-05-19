#!/usr/bin/python3


"""single link list module in python"""


class Node:
    """class Node for defining a single linked list"""

    def __init__(self, data, next_node=None):
        """initialization for class node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return data property when called"""
        return (self._data)

    @property
    def next_node(self):
        """returns next_node when called"""
        return (self._next_node)
    
    @data.setter
    def data(self, value):
        """sets the data for instance of Node"""
        if type(value) == int:
            self._data = value
        else:
            raise TypeError("data must be an integer")
        
    @next_node.setter
    def next_node(self, value):
        """sets the next_node for an instance of Node"""
        if type(value) == Node or value == None:
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """defines a single linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):

