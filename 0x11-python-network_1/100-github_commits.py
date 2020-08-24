#!/usr/bin/python3
""" connect to github api to get commits"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.\
          format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    for i, item in enumerate(r.json()):
        print("{}: {}".format(item.get("sha"),
              item.get("commit").get("author").get("name")))
        if i == 9:
            break
