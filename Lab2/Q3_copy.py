import random

d = dict()
d2 = dict()
n = int(input("How many elements:"))
print("Enter integers or strings")

sum = 0
l=0
for i in range(n):
    x = random.randrange(0,100)
    d[x] = (input("Enter the value:"))
    try:
        d[x] = int(d[x])
    except:
        d[x]
#calculating the average of the dict values
for i in d.keys():
    if isinstance(d[i], int) == True:
        sum = sum + d[i]
        l+=1
print("The average of the dictionary values is", sum/l)
        



#concatenating the strings
s = ""
for i in d.keys():
    if isinstance(d[i], str) == True:
        s = s+d[i]
print(d, "is the dictionary")
print(s,"is the concatenated string ")

#searching for the required string
srch = input("Enter the string to be searched:")
flag = 1
for i in d.keys():
    if d[i] == srch:
        print("Value found with key =", i)
        flag = 0
if flag == 1:
    print("Required string not found in the dictionary")

# searches for strings with only special characters
flag=0
for i in d.keys():
    flag=0
    if isinstance(d[i],str)== True:
        for letter in d[i]:
            if letter.isalnum() == False:
                continue
            else:
                flag=1
                break
        if flag == 0:
            print(d[i], end = ", ")
    
print("are the strings with special characters only")

