import urllib2
from bs4 import BeautifulSoup
import re
opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = "http://www.cnn.com/2013/11/30/us/nfl-bullying-jonathan-martin/index.html?hpt=hp_t3"

urlContent = opener.open(url).read()
soup = BeautifulSoup(urlContent)
title = soup.title.text

print title


body = soup.findAll('p')
	#body = body.encode('ascii','ignore')
outfile = open("/home/nilayan/Documents/Project/Python/AFINN-111.txt","r")
#print outfile
#outfile.read()
dictionary = {}
for item in outfile:
	#print item
	word = re.search("[a-zA-Z]*|\w",item)
	value = re.search("[-]?[0-9]",item)
	print word.group(0)+":"+value.group(0)
	dictionary[word.group(0)]=int(value.group(0))
#print dictionary
pos = 0
neg = 0
neutral = 0
value = 0
for i in body:
	sentence = str(i.text)
	#print sentence
	for word in sentence.split():
		#print word
		#print dictionary.get(word)
		if word in dictionary:
			value+=int(dictionary.get(word))
			print str(dictionary.get(word))
			print value
		else:
			pass
	#print value
if value > 0:
	pos +=1
elif value < 0:
	neg +=1
else:
	neutral +=1

print "Positive:"+str(pos)
print "Negative:"+str(neg)
print "Neutral:"+str(neutral)
print str(value)
