#!/usr/bin/python3
""" porst reques from url with requests lib"""

import requests
import sys


data = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=data)
print(r.text)
