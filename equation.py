import math
a=float(input("enter coefficient a:"))
b=float(input("enter coefficient b:"))
c=float(input("enter coefficient c:"))
d=(b**b)-4*a*c
D=math.sqrt (d)
if d==0:
    print("the equation has two equal roots")
elif d>0:
    print("the equation has two real roots")
elif d<0:
    print("the equation has two complex roots")
print("the roots are:\n")
r1=(-b-D)/2*a
r2=(-b+D)/2*a
print(r1,"\n")
print(r2,"\n")