
import urllib.request
from urllib.request import Request, urlopen

import lxml
import lxml.html
from lxml import etree as ET

tree = lxml.html.fromstring(open("./pages/abduction.txt").read())

c = tree.xpath('''//div[@id="related-entries"]/p[*]/a/@href''') 

print(c)
