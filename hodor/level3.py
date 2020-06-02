#!/usr/bin/python3
import pytesseract
import requests
from PIL import Image

url = 'http://158.69.76.135/level3.php'
image_url = 'http://158.69.76.135/captcha.php'
myobj = {
        'id': '1576',
        'holdthedoor': "Submit+Query",
        'key': None,
        'captcha': None
        }

myheader = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Referer": "http://158.69.76.135/level3.php"
            }

for i in range(1):
    
    session = requests.Session()
    #make get request to server
    r = session.get(url)
    
    #make request to get url_image
    img_data = session.get(image_url).content

    #save image to captcha.jpg
    with open('captcha.jpg', 'wb') as image:
        image.write(img_data)
    
    #open image and saves the text with tesseract
    image = Image.open('captcha.jpg')
    text = pytesseract.image_to_string(image)

    #save cookie to myobj in key variable
    myobj['key'] = r.cookies['HoldTheDoor']
    myobj['captcha'] = text
    
    #prints captcha
    print(text)
    
    #Post request
    x = session.post(url, data = myobj, headers = myheader, timeout=2.5)
    print(x.text)
