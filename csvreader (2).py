#import csv
import csv
with open('SentiWordNet.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		for block in row:
			print('').join(block)
		#print ('**').join(row)