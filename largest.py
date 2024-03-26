mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'positive numbers')

for i in range(size):
    data = int(input())
    mylist.append(data)

max = 0
for data in mylist:
    if data > max:
        max = data

print('The largest number in list is', max)
