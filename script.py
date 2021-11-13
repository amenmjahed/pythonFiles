myfile = open('myfile.txt','r')
myrows = myfile.readlines()
for row in myrows:
	print(row)