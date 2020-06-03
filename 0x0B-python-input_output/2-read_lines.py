#!/usr/bin/python3
"""
    function that reads n lines of a text file (UTF8)
    and prints it to stdout:

    Prototype: def read_lines(filename="", nb_lines=0):
    Read the entire file if nb_lines is lower or equal
    to 0 OR greater or equal to the total number of lines
    of the file
    You must use the with statement
    You don’t need to manage file permission or file doesn't
    exist exceptions.
"""


def read_lines(filename="", nb_lines=0):
    """ read nb_lines of a text """
    i = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            i += 1
        file.seek(0)
        if nb_lines <= 0 or nb_lines >= i:
            print(file.read())
        else:
            i = 0
            while i < nb_lines:
                print(file.readline().rstrip())
                i += 1
