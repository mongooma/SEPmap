import lxml
import lxml.html
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import urllib.request
from urllib.request import urlopen, Request
import multiprocessing
from multiprocessing import Pool
import time
from time import sleep
import sys
import nltk
from nltk.stem import WordNetLemmatizer



def extract():

	t = lxml.html.fromstring(open("mainpage.html").read()) # 

	# entries - XPATH: 
	# /html/body/div/div[3]/ul[1]/li[24]/ul/li[1]/a
	# /html/body/div/div[3]/ul[1]/li[1]/a

	entries = t.xpath("/html/body/div/div[3]/ul[*]/li[*]/ul/li[*]/a/@href") + \
			 t.xpath("/html/body/div/div[3]/ul[*]/li[*]/a/@href")

	return entries

def download(e):
	try:
		req = Request('https://plato.stanford.edu/%s' % e)
		req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0')
		resp = urlopen(req)
		content = resp.read()		
		with open("./pages/%s.txt" % e.split('/')[-2], 'w') as f:
			f.write(str(content))
		sleep(1/float(100))
	except:
		print("%s\n" % e, file=sys.stderr)

	return

def download_pages(entries):
	pool = Pool(processes = 5)
	for i in range(1200, len(entries), 100):
		pool.map(download, entries[i:i + 100])
		print("%s/%s\n" % (i,  len(entries)))
	pool.join()
	pool.close()

def user_tokenize(entries):
	#wnl = WordNetLemmatizer()
	with open("./pages/%s.txt" % e.split('/')[-2], 'w') as f:
		content = f.read()
		nltk.word_tokenize()



		

if __name__ == "__main__":

	entries = extract()
	# iteratively browse the child entries and get all the page
	download_pages(entries) # to ./pages
	
	# generate links
		# tokenize for each page
	user_tokenize(entries)
			# get rid of the high-frequency words (is, a, and...)
				# compare with wordnet result (keep the above average ones)
			# generate a dictionary for each entry

		# cross-ref the entries to form links
	link_formation(entries)
			# and make use of the "related entries" at the bottom of the page




