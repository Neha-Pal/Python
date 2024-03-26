number = int(input("Enter a positive number: "))
binary = 0
place = 1
n = number
while n>0:
    r = int(n % 2)
    binary = binary + r * place
    place = place*10
    n = n/2
print("Binary representaion of",number,"is",binary)