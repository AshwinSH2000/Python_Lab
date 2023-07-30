import random
def calcdiff(k, mega,x, oldmean):
	min_index = 0
	min_val = abs(x - oldmean[0])
	for i in range(k):
		diff = x - oldmean[i]
		if abs(diff)<min_val:
			min_val = abs(diff)
			min_index = i
	return min_index


k = int(input("Enter the number of clusters:"))
mega = []
oldmean = []

x = list(map(int, input("Enter all the data points:").split()))

ran = []

for i in range(k):
	r = random.randrange(0,len(x))
	if r not in ran:
		ran.append(r)
	else:
		r = random.randrange(0,len(x))
	oldmean.append(x[r])

	mega.append([])
	#print(mega)
	

for j in range(k**2):
	for i in x:
		index = calcdiff(k,mega, i, oldmean)
		mega[index].append(i)
		oldmean[index] = ( sum(mega[index])/len(mega[index]) )
	
#	print(oldmean)
	if j != ((k**2)-1):
		mega.clear()	
		for l in range(k):
			mega.append([])

#print(oldmean)

for i in range(k):
	print("Cluster {}".format(i+1))
	print(mega[i])
	
	
	
	
