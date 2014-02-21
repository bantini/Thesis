import urllib2
import re
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]
seed = "http://www.cnn.com"
url = [seed]
banned = []
robot = seed+"/robots.txt"

#Method to get the urls from robots.txt
def bannedContent(robot):	
	robotContent = opener.open(robot).read()
	for line in robotContent.splitlines():
		if "Disallow:" in line:
			line = line.replace("Disallow:","")
			line = line.lstrip()
			line = seed+line
			banned.append(line)

#Method to parse through the urls
def parser(link):
	urlContent = opener.open(link).read()
	soup = BeautifulSoup(urlContent)
	title = soup.title.text

#print title
	body = soup.findAll('a')
	#body = body.encode('ascii','ignore')

	for i in body:
		text = str(i.text.encode('ascii','ignore'))
		newurl=i.get('href')
		url.append(newurl)

#Main method
for link in url:
	if link in banned:
		pass
	else:
		try:
			if "http" in link:
				try:
					print link
					parser(link)
				except:
					pass
			else:
				link = seed+link
				if link in banned:
					pass
				else:
					try:
						print link
						parser(link)
					except:
						pass
		except:
			pass
