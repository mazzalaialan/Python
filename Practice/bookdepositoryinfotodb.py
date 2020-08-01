# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3
import re

conn = sqlite3.connect('bookdepositorydb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Books')
cur.execute('''
CREATE TABLE Books (titulo TEXT, precio INTEGER, moneda TEXT, link_imagen TEXT, descripcion TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.bookdepository.com/es/Dungeons-Dragons-Essentials-Kit-D-d-Boxed-Set-Wizards-RPG-Team/9780786966837?ref=pd_gw_1_pd_gateway_1_1' #input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve tags and values
h1tags = soup('h1')
for h1 in h1tags:
    if h1.get('itemprop', None)=='name':
        titulo = h1.contents[0]

spantags = soup('span')
lprecio = list()
for span in spantags:
    if type(span.get('class', None))==list:
        if span.get('class', None)[0] == 'sale-price':
            lprecio = str.split(span.contents[0],'$')
            moneda = lprecio[0]
            precio = float(re.sub('[,]', '.', re.sub('[.]', '', lprecio[1])))

imgtags = soup('img')
for img in imgtags:
    if type(img.get('class', None))==list:
        if img.get('class', None)[0]=='book-img':
            imagen = img.get('src', None)

divtags = soup('div')
for div in divtags:
    if div.get('itemprop', None)=='description':
        descripcion = ''
        for a in div.contents:
            None #descripcion = descripcion + a

cur.execute('''INSERT INTO Books (titulo, precio, moneda, link_imagen, descripcion)
            VALUES (?,?,?,?,?)''', (titulo,precio,moneda,imagen,descripcion))
conn.commit()

sqlstr = 'SELECT titulo, precio, moneda, link_imagen, descripcion FROM Books LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2], row[3], row[4])
cur.close()
