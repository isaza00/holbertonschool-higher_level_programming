#!/usr/bin/python3

import http.client, urllib.parse
import time

params = urllib.parse.urlencode({'id': '1687', 'holdthedoor': 'Submit+Query'})
headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
        }

for i in range(50):
    conn = http.client.HTTPConnection("158.69.76.135", timeout=2.5)


    conn.request("POST", "/level0.php", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    #time.sleep(0.5)

    #data = response.read()
    #print(data)

    conn.close()