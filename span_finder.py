import urllib.request, urllib.parse, urllib.error
import sys 
sys.path.append("C:\Python311\Lib\site-packages")
from bs4 import BeautifulSoup
import ssl

#adding code to bypass SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = (input('Enter something: '))
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')


# Retrieve all of the span tags
tags = soup('span')
count = 0
for tag in tags:
   http://py4e-data.dr-chuck.net/comments_1975971.html   
   count = count + int(tag.contents[0])
print(count)