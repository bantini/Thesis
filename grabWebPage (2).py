import urllib2
import re
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = ('http://www.cnn.com/2013/10/26/world/meast/iran-syria-talks/index.html#disqus_thread')


urlContent = opener.open(url).read()
soup = BeautifulSoup(urlContent)
title = soup.title.text



title =re.sub('[^A-Za-z0-1]','', title)
print title
# if "Myspace" in title:
# 	print "In myspace"
#body = soup.body.text
body = soup.findAll('p')
#body = body.encode('ascii','ignore')
outfile = open(title+".txt","w+")
for i in body:
	i=i.text.encode('ascii','ignore')
	outfile.write(i +'\n')
#print body
# else:
# 	print "Did not work"

#fileForURL = open("myspace.txt","w+")
#fileForURL.write(urlContent)
#fileForURL.close()
