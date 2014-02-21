import csv
import re
import urllib2
from bs4 import BeautifulSoup
from pylab import *
#The dictionary for the SentiWordNet wordlist
dictionary = {}

#Method to read the SentiWordNet.csv file and save the values in the dictionary
def sentiWordReader():
	with open('SentiWordNet.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			#print str(len(row))
			difference = float(row[2])-float(row[3])
			pattern = re.compile("[a-zA-Z\.]+[#][0-9]")
			matcher = re.findall(pattern,str(row))
			for match in matcher:
				wordPattern = re.compile("[a-zA-Z\.]+")
				wordMatcher = re.match(wordPattern,match)
				word = wordMatcher.group(0)
				dictionary[word.lower()] = difference

#Main method to grab the url and find the sentiments of each comment
def main():
	sentiWordReader()
	opener = urllib2.build_opener()
	url = "http://disqus.com/embed/comments/?disqus_version=82d70f54&base=default&f=cnn&t_i=%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_u=http%3A%2F%2Fwww.cnn.com%2F2013%2F12%2F01%2Fpolitics%2Fobamacare-website%2Findex.html&t_e=Administration%3A%20Obamacare%20website%20working%20smoothly&t_d=Administration%3A%20Obamacare%20website%20working%20smoothly&t_t=Administration%3A%20Obamacare%20website%20working%20smoothly&t_c=207582&s_o=default#2"
	urlcontent = opener.open(url).read()
	soup = BeautifulSoup(urlcontent)
	body = soup.findAll('p')
	pos = 0
	neg = 0
	neutral = 0
	for comment in body:
		sentence = str(comment.text.encode('ascii','ignore')).lower()
		value = 0.0
		for word in sentence.split():
			if word in dictionary:
				value += float(dictionary.get(word))
			else:
				pass 		
		if value < 0:
			neg+=1
		elif value > 0:
			pos+=1
		else:
			neutral+=1
	print "Number of positive comments:"+str(pos)
	print "Number of negative comments:"+str(neg)	
	print "Number of neutral comments:"+str(neutral)
	
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
#Calling the main method
main()		
