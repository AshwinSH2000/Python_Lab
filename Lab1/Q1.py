l1 = input("Enter the first list elements:")
l2 = input("Enter the second list elements:")

list1 = l1.split()
list2 = l2.split()
#convertins string to int
for i in range(len(list1)):
    list1[i] = int(list1[i])

for i in range(len(list2)):
    list2[i] = int(list2[i])

list3 = []

#selecting odd numbers from the first list
for i in list1:
    if i%2 == 1:
        list3.append(i)

#selecting even numbers from th e second list
for i in list2:
    if i%2 == 0:
        list3.append(i)

print("List 3 = odd elements of list1 + even elements of list 2")
print("list 3=",list3)
