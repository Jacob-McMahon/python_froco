import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

#adding code to bypass SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = (input('Enter URL: '))
data = urllib.request.urlopen(url, context = ctx).read()


print('Retrieved', len(data), 'characters')
datad = data.decode()
#print(datad)
tree = ET.fromstring(datad)
print(tree)

results = tree.findall('./comments/comment')
print(results, 'dang')

count = 0
for i in results:
    num = int(i.find('count').text)
    count = count + num
print(count)

