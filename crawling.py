#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

response =  urlopen('hm.daum.net')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("C:/WorkSpace/Python/새파일.txt", 'w')
for anchor in soup.select(".keyword"):
    data = print(str(i) + "위" + anchor.get_text())
    i = i + 1
    f.write(data)
f.close()