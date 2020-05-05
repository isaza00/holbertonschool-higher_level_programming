#!/usr/bin/python3


def multiple_returns(sentence):
    first = "None" if len(sentence) == 0 else sentence[0]
    new_tuple = (len(sentence), first)
    return new_tuple
