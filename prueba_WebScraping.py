import urllib.request
datos = urllib.request.urlopen('http://www.openwebinars.net').read().decode()

import sys
#!{sys.executable} -m pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
	print(tag.get('href'))