import time
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import datetime
import sqlite3
import nltk


try:
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent','Mozilla/5.0')]

except Exception, e:
	print "Error in Cookie"

try:
	conn = sqlite3.connect('knowledgebase.db')
	c = conn.cursor()
except Exception, e:
	print "Error in Connection"
	

def processor(data):
	try:
		tokenized = nltk.word_tokenize(data)
		tagged = nltk.pos_tag(tokenized)
		namedEnt = nltk.ne_chunk(tagged,binary = True)
		#print namedEnt
		#time.sleep(5)
		entities = re.findall(r'NE\s(.*?)/',str(namedEnt))
		descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))
		if len(entities) > 1:
			pass
		elif len(entities) == 0:
			pass
		else:
			print "--------------------"
			print 'Named:', entities[0]
			print "Description"
			for eachDesc in descriptives:
				print eachDesc
		#print entities
		
	except Exception, e:
		print "Failed while processing"
		print str(e)

def huffingtonRSSVisit():
	try:
		page = "http://feeds.huffingtonpost.com/huffingtonpost/raw_feed"
		sourceCode = opener.open(page).read()
		try:
			links = re.findall(r'<link.*href=\"(.*?)\"',sourceCode)
			for link in links:
				if '.rdf' in link:
					pass
				else:
					#print "The Link is :"
					#print "#############"
					linkSource = opener.open(link).read()
					linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource))
					for eachLine in linesOfInterest:
						if '<img width' in eachLine:
							pass
						elif '<a href=' in eachLine:
							pass
						else:
							processor(eachLine)
							#print eachLine
					
					time.sleep(5)
		except Exception, e:
			print "Failed inner loop"
			print str(e)
	except Exception, e:
		print "Failed Main loop"
		print str(e)

huffingtonRSSVisit()
