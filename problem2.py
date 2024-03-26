x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sign=-1
fact=1
i=2
sum=0
while i<=n:
    p=1
    fact=1
    for j in range(1,i+1):
        p = p*x
        fact = fact*j
        
    sum= sum + sign* p/fact
    sign = -1*sign
    i = i+2
print("cos(",x,") =",1+sum)