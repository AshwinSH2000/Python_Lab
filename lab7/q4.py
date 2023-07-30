import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 

def check(email):  
  
    if(re.search(regex,email)):  
        print("Valid Email")  
        return 1
          
    else:  
        print("Invalid Email") 
        return 0 

f1 = open("input.txt","w")
print("Enter email addresses and press enter after each. Type END when you want to stop")
x = input()
while(x!="END"):
	f1.write(x)
	f1.write("\n")
	x = input()
	
f1.close()

#now read and classify

f2 = open("input.txt","r")
f3 = open("valid.txt","w")
f4 = open("invalid.txt","w")
for line in f2:
	if check(line) == 1:
		f3.write(line)
	else:
		f4.write(line)
		
f2.close()
f3.close()
f4.close()

		
