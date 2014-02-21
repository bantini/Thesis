import urllib2
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
#opener.addheaders[('User-agent','Mozilla/5.0')]

url = "http://disqus.com/embed/comments/?disqus_version=82d70f54&base=default&f=cnn&t_i=%2F2013%2F11%2F30%2Fus%2Fnfl-bullying-jonathan-martin%2Findex.html&t_u=http%3A%2F%2Fwww.cnn.com%2F2013%2F11%2F30%2Fus%2Fnfl-bullying-jonathan-martin%2Findex.html&t_e=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_d=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_t=Dolphins%27%20Jonathan%20Martin%20will%20not%20return%20to%20NFL%20this%20season&t_c=207582&s_o=default#2"


urlContent = opener.open(url).read()
soup = BeautifulSoup(urlContent)
title = soup.title.text

print title


body = soup.findAll('p')
	#body = body.encode('ascii','ignore')
outfile = open("comments.txt","w+")

for i in body:
	text = str(i.text.encode('ascii','ignore'))
	#outfile.write(":::")
	outfile.write(text)
	#outfile.write("###")
	outfile.write("\n")
	#print i.text
	outfile.write("------------------")
#else:
#	print "Did not work"
outfile.close()
#fileForURL = open("myspace.txt","w+")
#fileForURL.write(urlContent)
#fileForURL.close()
