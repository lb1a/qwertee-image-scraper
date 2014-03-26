#!/usr/bin/python
#encoding=utf8
__author__ = 'lb'

import requests
from bs4 import BeautifulSoup
from os import path

r = requests.get('http://www.qwertee.com/')
soup = BeautifulSoup(r.text)

all = soup.find_all('div', 'buy')
for i in all:
    img = i.img.attrs['src']
    g = requests.get(r.url +i.img.attrs['src'])
    imgname = img.split('/')
    try:
        f = open(imgname[len(imgname)-1], 'w')
        f.write(g.content)
    except IOError:
        print "Failed to write image %s" % imgname[len(imgname)-1]
    finally:
        f.close()
