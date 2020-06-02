#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level2.php'

myobj = {
        'id': '1576',
        'holdthedoor': "Submit+Query",
        'key': None
        }

myheader = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Referer": "http://158.69.76.135/level2.php"
            }

for i in range(1):
    
    session = requests.Session()
    r = session.get(url)
    myobj['key'] = r.cookies['HoldTheDoor']
    x = session.post(url, data = myobj, headers = myheader, timeout=2.5)
    if i % 10 == 0:
        print(i)