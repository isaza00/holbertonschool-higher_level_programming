#!/usr/bin/python3
i = 1
for c in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print(chr(c).upper(), end="")
    else:
        print(chr(c).lower(), end="")
    i += 1

