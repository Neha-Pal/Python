

# print alternet elements QS 1

import numpy as np
mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter', str(size), 'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

print('Alternate elements are:')

for i in range(0, size, 2):
    print(mylist[i])


# reverse a list QS 2
mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter', str(size), 'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

# reverse the list
for i in range(size//2):
    # swapping elements
    mylist[i], mylist[len(mylist)-1-i] = mylist[len(mylist)-1-i], mylist[i]

print('Reverse list:', mylist)


# to display the largest no among the list QS 3

mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter', str(size), 'positive numbers')

for i in range(size):
    data = int(input())
    mylist.append(data)

max = 0
for data in mylist:
    if data > max:
        max = data

print('The largest number in list is', max)


# shifting a list QS 4

mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter', str(size), 'elements')

for i in range(size):
    data = input()
    mylist.append(data)

print('list before shifting', mylist)

temp = mylist[size-1]

for i in range(size-1, 0, -1):
    mylist[i] = mylist[i-1]

mylist[0] = temp

print('list after shifting', mylist)


# to dalete a given word from the string QS 5
text = input('Enter a string: ')
words = text.split()

data = input('Enter a word to delete: ')
status = False

for word in words:
    if word == data:
        words.remove(word)
        status = True

if status:
    text = ' '.join(words)
    print('String after deletion:', text)
else:
    print('Word not present in string.')


# to print the date from march 12,2022 QS 6

mydate = input('Enter a date(mm/dd/yyyy): ')
datelist = mydate.split('/')

month = int(datelist[0])
day = int(datelist[1])
year = int(datelist[2])

if month == 1:
    month = 'January'
elif month == 2:
    month = 'February'
elif month == 3:
    month = 'March'
elif month == 4:
    month = 'April'
elif month == 5:
    month = 'May'
elif month == 6:
    month = 'June'
elif month == 7:
    month = 'July'
elif month == 8:
    month = 'August'
elif month == 9:
    month = 'September'
elif month == 2:
    month = 'October'
elif month == 2:
    month = 'November'
elif month == 12:
    month = 'December'

newdate = month + ' ' + str(day) + ',' + str(year)

print(newdate)


# to capitalize a string QS 8

text = input("Enter a string:")
newtext = text.title()
print("The new string is:", newtext)


# to find the sum of each row of matrix of size m x m  QS 9

n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))

matrix = []

print("Enter values in matrix :")


for i in range(n):
    data = []
    for j in range(m):
        data.append(int(input()))
    matrix.append(data)


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()


for i in range(n):
    sum = 0
    for j in range(m):
        sum = sum + matrix[i][j]
    print('Sum of row', i+1, ':', sum)


# sum of two matrix QS 10

r1 = int(input("enter the no of rows in 1st matrix:"))
c1 = int(input("enter the no of columns of 1st matrix"))
matrix_1 = []
print("enter elements in 1st matrix:")
for i in range(r1):
    data = []
    for j in range(c1):
        data.append(int(input()))
    matrix_1.append(data)
for i in range(r1):
    for j in range(c1):
        print(matrix_1[i][j], end=' ')
    print()
r2 = int(input("enter the no of rows in 1st matrix:"))
c2 = int(input("enter the no of columns of 1st matrix"))
matrix_2 = []
print("enter elements in 2nd matrix:")
for i in range(r2):
    data = []
    for j in range(c2):
        data.append(int(input()))
    matrix_2.append(data)
for i in range(r2):
    for j in range(c2):
        print(matrix_2[i][j], end=' ')
    print()
result = [[0 for i in range(c1)] for i in range(r1)]
if r1 == r2 and c1 == c2:

    for i in range(r1):
        for j in range(c1):
            result[i][j] = matrix_1[i][j]+matrix_2[i][j]

print("The Sum of Above two Matrices is : ")
for r in result:
    print(r)


# to multiply two matrix QS 11

r1 = int(input("enter the no of rows in 1st matrix:"))
c1 = int(input("enter the no of columns of 1st matrix"))
matrix_1 = []
print("enter elements in 1st matrix:")
for i in range(r1):
    data = []
    for j in range(c1):
        data.append(int(input()))
    matrix_1.append(data)

for i in range(r1):
    for j in range(c1):
        print(matrix_1[i][j], end=' ')
    print()
r2 = int(input("enter the no of rows in 2nd matrix:"))
c2 = int(input("enter the no of columns of 2nd matrix:"))
matrix_2 = []
print("enter elements in 2nd matrix:")
for i in range(r2):
    data = []
    for j in range(c2):
        data.append(int(input()))
    matrix_2.append(data)
result = []
for i in range(r2):
    for j in range(c2):
        print(matrix_2[i][j], end=' ')
    print()
if (c1 == r2):
    result = np.dot(matrix_1, matrix_2)
else:
    print("multiplication is not possible...")
for r in result:
    print(r)
