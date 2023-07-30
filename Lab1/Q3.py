n = int(input("How many strings:"))
str = []
for i in range(n):
    x = input("Enter the string :")
    str.append(x)
    
print("The strings are:", end = " ")
print(str)

count = 0
for word in str:
    if len(word)>=2:
        if word[0] == word[len(word)-1]:
             count += 1
    if len(word) % 2 == 1:
        print(word, end = ", ")
print("are the strings having odd length.\n")
print(count, " words in the entered strings have the same first and last letters with length 2 or more.")
