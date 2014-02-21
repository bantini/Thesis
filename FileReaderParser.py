import nltk
import re
import time

exampleArray = ['The incredible intimidating NLP scares people who are sissies.']

##Let the fun begin##

def processLanguage():
	try:
		fileOpener = open("test.txt","r")
		for item in fileOpener:
			tokenized = nltk.word_tokenize(item)
			tagged = nltk.pos_tag(tokenized)
			for item in tagged:
				#tags = nltk.tag.str2tuple(tagged)
				if item[1] != "JJ":
					match = re.search(r"JJ?",item[1]);
					if match:
						print item[1]
			#chunkGram = r"""Chunk: {<RB\w?>*<VB\w?>*<NNP>}"""
			#chunkGram = r"""Chunk:{<JJ\w?>*<NN\w*>}"""
			#chunkParser = nltk.RegexpParser(chunkGram)
			#chunked = chunkParser.parse(tagged)
			#print chunked
			#chunked.draw()
			#time.sleep(555)			
			#print tagged
		
	except Exception, e:
		print str(e)


processLanguage()
