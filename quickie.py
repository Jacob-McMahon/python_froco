import urllib.request, urllib.parse, urllib.error
import json
import ssl


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    link = input('Enter location: ')
    if len(link) < 1: break

    params = dict()
    params['address'] = link
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    

   
    # print(json.dumps(js, indent=4))

    print(js['results'][0]['place_id'])

    