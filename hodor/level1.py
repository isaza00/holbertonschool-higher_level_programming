#!/usr/bin/python3
import requests
import time
import os

os.environ['no_proxy'] = '*'

url = 'http://158.69.76.135/level1.php'

myobj = {
        'id': '1576',
        'holdthedoor': "Submit+Query",
        'key': None
        }

for i in range(2):
    
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    myobj['key'] = r.cookies['HoldTheDoor']
    x = session.post(url, data = myobj, timeout=2.5)
    if i % 10 == 0:
        print(i)
