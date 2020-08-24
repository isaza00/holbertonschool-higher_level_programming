#!/usr/bin/python3
""" Write a Python script that print html status error """

import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
