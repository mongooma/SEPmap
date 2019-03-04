import lxml
import lxml.html
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import urllib.request
from urllib.request import urlopen, Request


def extract():

	t = lxml.html.fromstring(open("mainpage.html").read()) # 

	# print(t.xpath("/html/body/div/div[3]/ul[*]/li[*]/ul/li[*]/a/@href"))
	# entries - XPATH: 
	# /html/body/div/div[3]/ul[1]/li[24]/ul/li[1]/a
	# /html/body/div/div[3]/ul[1]/li[1]/a

	entries = t.xpath("/html/body/div/div[3]/ul[*]/li[*]/ul/li[*]/a/@href") + \
			 t.xpath("/html/body/div/div[3]/ul[*]/li[*]/a/@href")

	return entries



if __name__ == "__main__":

	entries = extract()
	















	# iteratively browse the child entries and get all the page

	# generate links
		# tokenize for each page
			# get rid of the high-frequency words (is, a, and...)
				# compare with wordnet result (keep the above average ones)
		# generate a dictionary for each entry
		# cross-ref the entries to form links
		# make use of the "related entries" at the bottom of the page




