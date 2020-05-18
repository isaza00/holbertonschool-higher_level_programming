#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        value = True
    except ValueError:
        value = True
    return (value)
