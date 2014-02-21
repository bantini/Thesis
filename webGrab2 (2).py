import urllib2
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = "http://en.wikipedia.org/wiki/Bayside_(band)"


urlContent = opener.open(url).read()
soup = BeautifulSoup(urlContent)
title = soup.title.text

print title


body = soup.findAll('p')
	#body = body.encode('ascii','ignore')
outfile = open("bayside.txt","w+")

for i in body:
		#i.encode('ascii','ignore')
	outfile.write(i.text +'\n')
	#print body
else:
	print "Did not work"

#fileForURL = open("myspace.txt","w+")
#fileForURL.write(urlContent)
#fileForURL.close()
