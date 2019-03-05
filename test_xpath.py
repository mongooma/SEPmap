from lxml import etree
import lxml.html

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import re

t = lxml.html.fromstring(open("pages/abrabanel.txt").read()) # 


content = t.xpath('''//p''')

for c in content: 
	c = re.sub(r'\\n', ' ', c.text_content())
	with open("log.txt", "a") as f:
		f.write(str(c) + '\n')


# print(content)


# for c in content:
# 	try:
# 		txt = re.sub("\n", ' ', c.text)
# 		raw_words = re.findall(r"[\w|-]+", txt) # words & hyphens	
# 	except:
# 		pass
# 	print(raw_words[:10])


