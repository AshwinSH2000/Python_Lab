x = input("Enter the list elements:")
l1 = x.split()

#str to int
for i in range(len(l1)):
    l1[i] = int(l1[i])

a = dict()
for i in l1:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
newlist = []
for keys in a:
    if a[keys] == 1:
        newlist.append(keys)
print("The unique elements are ",newlist)
