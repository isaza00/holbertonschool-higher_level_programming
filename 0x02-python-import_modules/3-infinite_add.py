#!/usr/bin/python3


def infinite(args):
    sum = 0
    for a in args[1:]:
        sum += int(a)
    print(sum)

if __name__ == "__main__":
    import sys
    infinite(sys.argv)
