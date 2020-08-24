#!/usr/bin/python3
""" connect to github api to get id via personal token"""
import requests
import sys


auth = (sys.argv[1], sys.argv[2])
r = requests.get('https://api.github.com/user', auth=auth)
print(r.json().get('id'))
