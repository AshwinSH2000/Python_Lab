def multiply(l1):
    res = 1
    for num in l1:
        res = res * num

    return res

x = input("Enter the elements of the list:")
list1 = x.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])

print("Result of multiplication of each element of the list = ", multiply(list1))

    
