from bs4 import BeautifulSoup
import requests
import smtplib
import urllib.request
import os


url = "https://www.amazon.sa/-/en/dp/1989025013/?coliid=IM3HFYYKLCALN&colid=37C2CZ1721GPP&psc=1&ref_=lv_ov_lig_dp_it"
r = requests.get(url)

page = requests.get(url,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html5lib")

find_price = soup.find(id="price")
price = find_price.getText()

a = price.split()

price_as_float = a[1]

price_as_float = float(price_as_float)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    # send email
    pass

# get the image and save it


find_img = soup.select_one(selector="#imgBlkFront")

all_images = []
for img in soup.findAll('img'):
    all_images.append(img.get('src'))

img = all_images[5]

url = img
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = 'img{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)