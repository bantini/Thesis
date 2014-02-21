import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

urls = [url]  # urls to scrape
visited = [url]  # historic record

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
        soup = BeautifulSoup(htmltext)
    	urls.pop(0)

    	print soup.findAll ('a', href = True)
    	#for tag in soup.findAll('a', href = True):
    	#	print tag
    except:
        print urls[0]
    







