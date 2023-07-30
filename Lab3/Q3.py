#write a python program to detect all local variables in a function
def myfunction():
    a = 12.34
    b = str
    x = 5

str = 'hello'
myfunction()
print("The number of local variables = ",myfunction.__code__.co_nlocals) 
 
