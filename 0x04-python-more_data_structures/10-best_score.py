#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return (sorted((value, key) for (key, value) in a_dictionary.items()).pop()[1])
