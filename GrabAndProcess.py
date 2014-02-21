import urllib2
from bs4 import BeautifulSoup
import re
opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = "http://disqus.com/embed/comments/?disqus_version=82d70f54&base=default&f=cnn&t_i=%2F2013%2F11%2F30%2Fus%2Fnfl-bullying-jonathan-martin%2Findex.html&t_u=http%3A%2F%2Fwww.cnn.com%2F2013%2F11%2F30%2Fus%2Fnfl-bullying-jonathan-martin%2Findex.html&t_e=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_d=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_t=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_c=207582&s_o=default#2"


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
	#print word.group(0)+":"+value.group(0)
	lower = word.group().lower()
	dictionary[lower]=int(value.group(0))
#print dictionary
pos = 0
neg = 0
neutral = 0
for i in body:
	sentence = i.text.encode('ascii','ignore')
	value = 0
	for word in sentence.split():
		#print word
		#print dictionary.get(word)
		lowerWord = word.lower()
		if lowerWord in dictionary:
			value+=int(dictionary.get(lowerWord))
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

