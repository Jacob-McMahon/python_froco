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
for tag in tags:
   # Look at the parts of a tag
   print ('TAG:',tag)
   print ('URL:',tag.get('href', None))
   print ('Contents:',tag.contents[0])
   print ('Attrs:',tag.attrs)