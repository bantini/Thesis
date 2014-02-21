file = open('/home/nilayan/Project/test.txt','w')

file.write("Hello this is a file")
file.close()

readFile = open('/home/nilayan/Project/test.txt').read()

print readFile
