import numpy as np
r1=int(input("enter the no of rows in 1st matrix:"))
c1=int(input("enter the no of columns of 1st matrix"))
matrix_1= []
print("enter elements in 1st matrix:")
for i in range(r1):
    data=[]
    for j in range(c1):
        data.append(int(input()))
    matrix_1.append(data)

for i in range(r1):
    for j in range(c1):
        print(matrix_1[i][j],end=' ')
    print()
r2=int(input("enter the no of rows in 2nd matrix:"))
c2=int(input("enter the no of columns of 2nd matrix"))
matrix_2= []
print("enter elements in 2nd matrix:")
for i in range(r2):
    data=[]
    for j in range(c2):
        data.append(int(input()))
    matrix_2.append(data)
result= []
for i in range(r2):
    for j in range(c2):
        print(matrix_2[i][j],end=' ')
    print()
if(c1==r2):
    result = np.dot(matrix_1, matrix_2)
else:
    print("multiplication is not possiblw...")
for r in result:
    print(r)



    
