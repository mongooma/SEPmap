from lxml import etree
import lxml.html

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


t = lxml.html.fromstring(open("mainpage.html").read()) # 

print(t.xpath("/html/body/div/div[3]/ul[*]/li[*]/ul/li[*]/a/@href"))

entries = t.xpath("/html/body/div/div[3]/ul[*]/li[*]/ul/li[*]/a/@href") + t.xpath("/html/body/div/div[3]/ul[*]/li[*]/a@href")

