import re
import time as time

file1 = open("thanksgiving.csv","r")
file2 = open("thanks_clean.txt","w")
for text in file1:
	text = re.sub("[h][t][t][p].*[^\b]"," ",text)
	text = re.sub("[\][u][a-z0-9]{4}","", text)
	text = re.sub("[\.;,]"," ",text)
	temp = text.split()
	if temp < 3:
		pass
	else:	
		text = text.encode('ascii','ignore')
		file2.write(text)
