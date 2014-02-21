import nltk
import re
import time
import urllib2
from bs4 import BeautifulSoup

##Let the fun begin##

def processLanguage():
	try:
		opener = urllib2.build_opener()
		#opener.addheaders[('User-agent','Mozilla/5.0')]

		url = "http://disqus.com/embed/comments/?disqus_version=82d70f54&base=default&f=cnn&t_i=%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_u=http%3A%2F%2Fwww.cnn.com%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_e=Administration%3A%20Obamacare%20website%20working%20smoothly&t_d=Administration%3A%20Obamacare%20website%20working%20smoothly&t_t=Administration%3A%20Obamacare%20website%20working%20smoothly&t_c=207582&s_o=default#2"

		urlContent = opener.open(url).read()
		soup = BeautifulSoup(urlContent)
		title = soup.title.text


		body = soup.findAll('p')	

		for item in body:
			#print item
			sentence = item.text.encode('ascii','ignore')
			#print sentence
			tokenized = nltk.word_tokenize(sentence)
			tagged = nltk.pos_tag(tokenized)
			namedEntity = nltk.ne_chunk(tagged,binary=True)
			compiler = re.compile("[(]['][a-zA-Z]+[']")
			for chunks in namedEntity:
				#print chunks[0]
				if compiler.match(str(chunks[0])):
					chunk = str(chunks[0])
					front = chunk[2:]
					word = re.search("[a-zA-Z]+[']",front)
					print word.group(0)[:-1]
					#print "Matched"
			#namedEntity.draw()
				
	except Exception, e:
		print str(e)


processLanguage()
