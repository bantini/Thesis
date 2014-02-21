import urllib2
from bs4 import BeautifulSoup
import re
from pylab import *
opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = "http://disqus.com/embed/comments/?disqus_version=82d70f54&base=default&f=cnn&t_i=%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_u=http%3A%2F%2Fwww.cnn.com%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_e=Administration%3A%20Obamacare%20website%20working%20smoothly&t_d=Administration%3A%20Obamacare%20website%20working%20smoothly&t_t=Administration%3A%20Obamacare%20website%20working%20smoothly&t_c=207582&s_o=default#2"

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
	
#Drawing the pie chart
total = pos+neg+neutral
print total
pos_percent = 100*pos
pos_percent = pos_percent/total
neg_percent = 100*neg
neg_percent = neg_percent/total
neutral_percent = 100*neutral
neutral_percent = neutral_percent/total
figure(1, figsize= (6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])
labels = 'Positive:'+str(pos_percent)+"%", 'Negative:'+str(neg_percent)+"%", 'Neutral:'+str(neutral_percent)+"%"
colors = ["green","red","white"]
fracs= [pos_percent, neg_percent, neutral_percent]
pie(fracs, labels = labels, colors = colors)
show()

print "Positive:"+str(pos)
print "Negative:"+str(neg)
print "Neutral:"+str(neutral)

