#!/usr/bin/python3
""" fetches X-Request-Id from headers with requests lib"""

import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
