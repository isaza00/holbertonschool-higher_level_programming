#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status with requests lib"""

import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
