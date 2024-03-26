r = int(input("Enter the number of rows:")) 
c = int(input("Enter the number of columns:")) 
  
matrix = [] 

print("Enter values in matrix :") 

# For user input 
for i in range(r):
    data =[] 
    for j in range(c):
         data.append(int(input())) 
    matrix.append(data) 

# For printing the matrix 
for i in range(r): 
    for j in range(c): 
        print(matrix[i][j], end = " ") 
    print()


# For printing row wise sum 
for i in range(r):
    sum = 0
    for j in range(c): 
        sum = sum + matrix[i][j]
    print('Sum of row',i+1,':',sum) 
