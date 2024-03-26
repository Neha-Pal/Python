"""num=int(input("enter a number:"))
if num<0:
    print("please enter a valid number.")
elif num==0:
    print(1)
else:
    factorial=1
while num>1:
    factorial=factorial*num
    num=num-1
print("Factorial of",num,"is",factorial)

#using iterative function

def factorial(n):
    
    factorial=1
    for i in range(n):
        factorial=factorial*(i+1)
    return factorial
num=int(input("enter a number:"))
print("the factorial of the number is:",factorial(num))    
"""

#using recursive function

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
num=int(input("enter a number:"))
print("factorial of the number is:",fac(num))