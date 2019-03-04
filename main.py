import bs4
import lxml


def download(path):
	# download the page to local file
	with open("%s.txt" % (path.split('/')[-1]), 'w') as f
		f.write(str(urllib.request.urlopen(path).read()))

def search(path):
	try:

		return 1
	except:
		return 0

def extract(soup):
	i = 0
	j = 0
	k = 0
	l = 0

	found = -1
	bottom = False;
	while(1):
		found = search("/html/body/div/div[3]/ul[%s]" % i) # content
		if found:
			while(1):
				found = search("/html/body/div/div[3]/ul[%s]/li[%s]" % (i, j))
				if found:
					while(1):
						found = search("/html/body/div/div[3]/ul[%s]/li[%s]/ul/li[%s]" % (i, j, k))
						if found:
							bottom = True # find a second level list
							download("/html/body/div/div[3]/ul[%s]/li[%s]/ul/li[%s]/a.href" % (i, j, k))
						else:
							break
						k += 1

					if bottom == False： # only have the first level list
						download("/html/body/div/div[3]/ul[%s]/li[%s]/a.href" % (i, j))
				else:
					break
				j += 1
		else:
			break
		i += 1




if __name__ == "__main__":

	# get the main page of SEP

	main_p = "https://plato.stanford.edu/contents.html"
	# soup = bs4.BeautifulSoup(urllib.request.urlopen(main_p).read())
	content = open("mainpage.html").read()

	# entries - XPATH: 
	# /html/body/div/div[3]/ul[1]/li[24]/ul/li[1]/a
	# /html/body/div/div[3]/ul[1]/li[1]/a













	# iteratively browse the child entries and get all the page

	# generate links
		# tokenize for each page
			# get rid of the high-frequency words (is, a, and...)
				# compare with wordnet result (keep the above average ones)
		# generate a dictionary for each entry
		# cross-ref the entries to form links
		# make use of the "related entries" at the bottom of the page




