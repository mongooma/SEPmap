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
import re
import pickle as pkl
import networkx as nx


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
		print("download:%s\n" % e, file=sys.stderr)

	return

def download_pages(entries):
	pool = Pool(processes = 5)
	for i in range(0, len(entries), 100):
		pool.map(download, entries[i:i + 100])
		print("%s/%s\n" % (i,  len(entries)))
	pool.join()
	pool.close()

def get_raw_words(entries):
	'''
	(not tokenizing!)
	'''
	for e in entries:
		try:
			with open("./pages/%s.txt" % e.split('/')[-2]) as f1, \
				 open("./raw_words/%s.txt" % e.split('/')[-2], 'w') as f2:
				t = lxml.html.fromstring(f1.read())
				content = t.xpath('''//p''')
				for c in content:
					c = re.sub(r'\\n', ' ', c.text_content())
					raw_words = re.findall(r"[\w|-]+", c) # words & hyphens
					for w in raw_words:
						f2.write(str(w) + '\n')
		except:
			print("get_raw_words:%s\n" % e, file=sys.stderr)

	return 

def link_formation_related(entries, dictionary):
	'''
	Only extract the "related entries" at the bottom of the page
	'''
	for e in entries:
		key = e.split('/')[-2]
		try:
			with open("./pages/%s.txt" % e.split('/')[-2]) as f1:
				t = lxml.html.fromstring(f1.read())
				content = t.xpath('''//div[@id="related-entries"]/p[*]/a/@href''') 
				for c in content:
					#print(c)
					dictionary.setdefault(key, [])
					dictionary[key].append(c.split('/')[-2])
		except:
			print("link_formation_related:%s\n" % e, file=sys.stderr)

def generate_graph(dictionary):
	'''
	Using networkx;
	node name as entry name
	'''
	g = nx.from_dict_of_lists(dictionary, create_using=nx.Graph())
	nx.write_edgelist(g, "./graph.csv", comments='#', delimiter=',', data=True, encoding='utf-8')


if __name__ == "__main__":

	entries = extract()
	# iteratively browse the child entries and get all the page
	#download_pages(entries) # to ./pages
	
	# generate links
		# tokenize for each page
	#get_raw_words(entries)
			# get rid of the high-frequency words (is, a, and...)
				# compare with wordnet result (keep the above average ones)
			# generate a dictionary for each entry

		# cross-ref the entries to form links
	#dictionary = dict()
	#link_formation_related(entries, dictionary)
			# and make use of the "related entries" at the bottom of the page
	#pkl.dump(dictionary, open("./dic.pkl", 'wb'), protocol=2)
	dictionary = pkl.load(open("./dic.pkl", 'rb'))
	generate_graph(dictionary)






