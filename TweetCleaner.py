import json
file1 = file("oklahoma.txt","r")
for text in file1:
	info = json.loads(text)
	if 'text' in info: 
		tweet = info['text']
		print tweet+"\n" 
