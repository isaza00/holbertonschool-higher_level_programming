#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    sign = 1
    lista = []
    for x in roman_string[::-1]:
        if x in d:
            lista.append(d[x])
    for index, i in enumerate(lista[:-1]):
        if i <= lista[index + 1]:
            suma += i * sign
            sign = 1
        else:
            suma += i * sign
            sign *= -1
    suma += lista[-1] * sign
    return (suma)
