
import lxml
from lxml import etree

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import urllib.request
from urllib.request import urlopen, Request

req = Request('https://plato.stanford.edu/contents.html')
req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0')
resp = urlopen(req)
content = resp.read()


print(content)


#tree = etree.parse(StringIO(str(content)))

