#!/usr/bin/python3
""" porst reques from url with params in url"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    if not r.json():
        print("No result")
    else:
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
