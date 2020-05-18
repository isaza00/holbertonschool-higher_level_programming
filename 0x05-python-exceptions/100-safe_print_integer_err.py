#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        value = True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        value = False

    return (value)
