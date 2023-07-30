fo = open("file3.txt", "w")
print("Enter the text you want to save in the file(hit enter after typing each line, type END to stop entering) :")
x = input()
while(x != "END"):
	fo.write(x)
	fo.write("\n")
	x = input()

fo.close()

fp = open("file3.txt","r")
file_text = fp.readlines()
#file_text = file_text.split()
print("\n\nThe contents of the file is:",file_text)	

print("reverse of the file is:")
for i in file_text[::-1]:
	print(i, end = "")
