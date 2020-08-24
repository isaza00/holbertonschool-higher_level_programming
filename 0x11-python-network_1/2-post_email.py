#!/usr/bin/python3
""" Write a Python script that post to url"""

import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
