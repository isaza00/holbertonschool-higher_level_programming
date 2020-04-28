#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for c in range(len(str)):
        if ord(str[c]) > 96 and ord(str[c]) < 123:
            str2 += (chr(ord(str[c]) - 32))
        else:
            str2 += str[c]
    print (str2)
