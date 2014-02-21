import nltk
import re
import time

#exampleArray = ['The incredible intimidating NLP scares people who are sissies.']
exampleArray = ['The iPhone is a good phone']

##Let the fun begin##
fileopener = open("syria.txt","r")

def processLanguage():
	try:
		for item in fileopener:
			#print item
			tokenized = nltk.word_tokenize(item)
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
