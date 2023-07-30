import re 
   
regex = r'^[a-z]$|^([a-z]).*\1$'
x = input("Enter any string:")

if(re.search(regex, x)):   
    print("Starts and ends with the same characters")   
else:   
    print("Starts and ends with different characters")   
