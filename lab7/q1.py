f = open("q1.txt","w")
f.write("Hello my name is ashwin\n")
f.write("This is my laptop and it is HP\n")
f.write("I dont know what more to write in the file\n")
f.close()


file = open("q1.txt", "r")


number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
  line = line.strip("\n")
								#won't count \n as character

  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)
  
file.close()

print("words = {}".format(number_of_words))
print("chars = {}".format(number_of_characters))
print("lines = {}".format(number_of_lines))


