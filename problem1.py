x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sign = -1
fact = i =1
sum = 0
while i<=n:
    p = 1
    fact = 1
    for j in range(1,i+1):
        p = p*x
        fact = fact*j
    sign = -1*sign
    sum = sum + sign* p/fact
    i = i+2
print("sin(",x,") =",sum)