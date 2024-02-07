import urllib.request, urllib.parse, urllib.error
import sys 
sys.path.append("C:\Python311\Lib\site-packages")
from bs4 import BeautifulSoup
import ssl

#adding code to bypass SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



#adding code to bypass SSL cert error
url = input('Enter things: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

lst = list()
for i in tags:
    lst.append(i.get('href', None))
print(lst)
