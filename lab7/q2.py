fo = open("fil12.txt","w")
print("Enter the text you want to save in the file(hit enter after typing each line, type END to stop entering) :")
x = input()
'''while(x != "END"):
	fo.write(x)
#	fo.write("\n")
	x = input()	'''

fo.write(x)
fo.close()

fp = open("fil12.txt","r")
file_text = fp.read()
file_text = file_text.split()
print("\n\nThe contents of the file is:",file_text)

d = dict()
for word in file_text:
	if word not in d:
		d[word] = 1
	else:
		d[word] += 1
		
for keys in d:
	print(" {} : {}".format(keys, d[keys]))
