#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    if n >= 0 and n < len(str):
        for i in range(n + 1):
            if n != i:
                str2 += str[i]
        for i in range(n + 1, len(str)):
            str2 += str[i]
        return str2
    return str
