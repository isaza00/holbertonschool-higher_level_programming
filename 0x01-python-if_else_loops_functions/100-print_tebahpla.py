#!/usr/bin/python3
i = 1
for c in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        char = chr(c).upper()
    else:
        char = chr(c).lower()
    print(char, end="")
    i += 1
