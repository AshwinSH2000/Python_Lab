r1 = int(input("Enter the row of the first matrix:"))
c1 = int(input("Enter the column of the first matrix:"))
r2 = int(input("Enter the row of the second matrix:"))
c2 = int(input("Enter the column of the second matrix:"))

matrix1 = []
matrix2 = []
print("Enter the entries rowwise of matrix 1:") 
  
# For user input 
for i in range(r1):          # A for loop for row entries 
    a =[] 
    for j in range(c1):      # A for loop for column entries 
         a.append(int(input())) 
    matrix1.append(a)


        
for i in range(r1): 
    for j in range(c1): 
        print(matrix1[i][j], end = " ") 
    print() 

print("Enter the entries rowwise of matrix 2:") 
  
# For user input 
for i in range(r2):          # A for loop for row entries 
    a =[] 
    for j in range(c2):      # A for loop for column entries 
         a.append(int(input())) 
    matrix2.append(a)


        
for i in range(r2): 
    for j in range(c2): 
        print(matrix2[i][j], end = " ") 
    print()


d1 = dict()
d2 = dict()
for i in range(r1):
    for j in range(c2):
        if matrix1[i][j] != 0:
            d1[ (i,j) ] = matrix1[i][j]

for i in range(r2):
    for j in range(c2):
        if matrix2[i][j] != 0:
            d2[ (i,j) ] = matrix2[i][j]
d3 = dict()

for i in d1.keys():
    if i in d2:
        d3[i] = d1[i] + d2[i]
    else:
        d3[i] = d1[i]
        
for i in d2.keys():
    if i not in d2:
        d3[i] = d2[i]


    

print("dict 1", d1)
print("dict 2",d2)
print("dict 3 = sum = ", d3)

print("The sum in matrix form is ")
for i in range(r1):
    for j in range(c1):
        try:
            print( d3[ (i,j) ] , end = " ")
        except:
            print( 0, end = " ")
    print()
            
