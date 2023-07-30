import random

d = dict()
d2 = dict()
n = int(input("How many elements:"))
print("Enter integers only")

sum = 0
for i in range(n):
    x = random.randrange(0,100)
    d[x] = int(input("Enter the value:"))

#calculating the average of the dict values
for i in d.keys():
    sum += d[i]
print("The average of the dictionary values is", sum/len(d))
        

n = int(input("How many elements:"))
print("Enter strings only")

sum = 0
for i in range(n):
    x = random.randrange(0,100)
    d2[x] = input("Enter the value:")

#concatenating the strings
s = ""
for i in d2.keys():
    s = s+d2[i]
print(d2, "is the dictionary")
print(s,"is the concatenated string ")

#searching for the required string
srch = input("Enter the string to be searched:")
flag = 1
for i in d2.keys():
    if d2[i] == srch:
        print("Value found with key =", i)
        flag = 0
if flag == 1:
    print("Required string not found in the dictionary")

# searches for strings with only special characters
flag=0
for i in d2.keys():
    flag=0
    for letter in d2[i]:
        if letter.isalnum() == False:
            continue
        else:
            flag=1
            break
    if flag == 0:
        print(d2[i], end = ", ")
    
print("are the strings with special characters only")

