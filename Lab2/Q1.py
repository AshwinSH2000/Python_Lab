'''
sen = input("Enter any sentence:")
d = dict()
for letter in sen:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1

print(d[' ']+1, "is the number of words in the sentence")

'''
sen = input("Enter any sentence:")
d = dict()
sen = sen.split()
for word in sen:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
count = 0
for keys in d:
    count += d[keys]

print(count)


