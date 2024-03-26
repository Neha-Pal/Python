import math
p=int(input("enter principle:\n"))
t=int(input("enter time:\n"))
r=float(input("enter rate of interest:\n"))
c=p*(1+r/100)**t-p
print("the compound interest is:",c)