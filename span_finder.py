
# Retrieve all of the anchor tags
tags = 1 #soup('span')
for tag in tags:
   # Look at the parts of a tag
   print ('TAG:',tag)
   print ('URL:',tag.get('href', None))
   print ('Contents:',tag.contents[0])
   print ('Attrs:',tag.attrs)