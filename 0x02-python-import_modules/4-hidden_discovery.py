#!/usr/bin/python3.4
import hidden_4


def print_hidden():
    hidden = dir(hidden_4)
    for i in hidden:
        if(i[:2] != "__"):
            print(i)

if __name__ == "__main__":
    print_hidden()
