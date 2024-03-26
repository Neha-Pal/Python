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
r2=int(input("enter the no of rows in 1st matrix:"))
c2=int(input("enter the no of columns of 1st matrix"))
matrix_2= []
print("enter elements in 2nd matrix:")
for i in range(r2):
    data=[]
    for j in range(c2):
        data.append(int(input()))
    matrix_2.append(data)
for i in range(r2):
    for j in range(c2):
        print(matrix_2[i][j],end=' ')
    print()
result=[[0 for i in range(c1)] for i in range(r1)]
if r1==r2 and c1==c2:
    
    for i in range(r1):
        for j in range(c1):
            result[i][j] = matrix_1[i][j]+matrix_2[i][j]
           
print("The Sum of Above two Matrices is : ")
for r in result:
    print(r)