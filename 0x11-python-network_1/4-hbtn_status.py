#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status with requests lib"""

import requests


r = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: <class 'bytes'>\
       \n\t- content: {}".format(r.text))
