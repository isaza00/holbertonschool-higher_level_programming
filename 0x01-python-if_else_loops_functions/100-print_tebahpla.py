#!/usr/bin/python3
for c in range(26, 0, -1):
    if c % 2 == 0:
        print("{:c}".format(c + 96), end="")
    else:
        print("{:c}".format(c + 64), end="")
