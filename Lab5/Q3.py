class unique_num:
    num = []
    all_subs = []
    def __init__(self, num):
        self.num = num
    def powerset(self,seq):
        #in all cases, one entry will be null set and the other entire set
        
        if len(seq)<=1:
            yield seq
            yield []
        else:
            for item in self.powerset(seq[1:]):
                yield [seq[0]]+item
                yield item


n = input("Enter unique numbers:")
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])
num_class = unique_num(n)
x = [l for l in num_class.powerset(n)]
print(x)


'''self.all_subs.append(self.num)
        self.all_subs.append([])
        
        a = []
        for i in range(1,len(self.num)+1):
            a = []
            for j in self.num:
                if j not in a:
                    a.append(j)
                    if len(a) == i:
                        if a not in self.all_subs:
                            self.all_subs.append(a)
                            a = []
                        else:
                            a.pop()
                            
        print(self.all_subs)'''
