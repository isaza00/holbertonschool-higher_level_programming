#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if ord(c) > 96 and ord(c) < 123:
            char = ord(c) - 32
        print("{:c}".format(char), end="")
    print()
