# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.bookdepository.com/es/Dungeons-Dragons-Essentials-Kit-D-d-Boxed-Set-Wizards-RPG-Team/9780786966837?ref=pd_gw_1_pd_gateway_1_1' #input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve tags and values
divtags = soup('h1')
for tag in divtags:
    if tag.get('itemprop', None)=='name':
        print('Titulo: ',tag.contents[0])

spantags = soup('span')
for tag in spantags:
    if type(tag.get('class', None))==list:
        if tag.get('class', None)[0] == 'sale-price':
            print('Precio: ',tag.contents[0])

imgtags = soup('img')
for tag in imgtags:
    if type(tag.get('class', None))==list:
        if tag.get('class', None)[0]=='book-img':
            #print(tag.get('alt', None))
            print('imagen: ',tag.get('src', None))

divtags = soup('div')
for tag in divtags:
    if tag.get('itemprop', None)=='description':
        print('Descripcion: ')
        for a in tag.contents:
            print(a)
