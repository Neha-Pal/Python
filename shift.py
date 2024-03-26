mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'elements')

for i in range(size):
    data = input()
    mylist.append(data)
    
print('list before shifting', mylist)

temp = mylist[size-1]

for i in range(size-1,0,-1):
    mylist[i] = mylist[i-1]

mylist[0] = temp

print('list after shifting', mylist)