binary = input("Enter a binary number: ")
decimal=0
place=0
for i in reversed(binary):
    decimal = decimal + int(i)*pow(2,place)
    place=place+1
print("Decimal representation of binary",binary,"is",decimal)
