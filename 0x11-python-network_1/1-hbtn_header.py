#!/usr/bin/python3
""" Write a Python script that shows
    X-Request_Id Header of an URL """

import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
