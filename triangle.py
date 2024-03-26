
a=int(input("enter 1st length of side of the triangle:"))
b=int(input("enter 2nd length of side of the triangle:"))
c=int(input("enter 3rd length of side of the triangle:"))
s=(a+b+c)/2
area=float((s*(s-a)*(s-b)*(s-c))**0.5)
print("the area is:",area)