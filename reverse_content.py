mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',size,'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

#reverse the list
for i in range(size//2):
    #swapping elements
    mylist[i],mylist[len(mylist)-1-i] = mylist[len(mylist)-1-i], mylist[i]

print('Reverse list:', mylist)