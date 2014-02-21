import nltk
import re
import time

exampleArray = ['The incredible intimidating NLP scares people who are sissies.']

##Let the fun begin##

def processLanguage():
	try:
		for item in exampleArray:
			tokenized = nltk.word_tokenize(item)
			tagged = nltk.pos_tag(tokenized)
			#chunkGram = r"""Chunk: {<RB\w?>*<VB\w?>*<NNP>}"""
			#chunkGram = r"""Chunk:{<JJ\w?>*<NN\w*>}"""
			chunkGram =r"""
	Chunk:
		{<.*>}
		}<RB|NNS>{
		"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			print chunked
			chunked.draw()
			#time.sleep(555)			
			print tagged
		
	except Exception, e:
		print str(e)


processLanguage()
