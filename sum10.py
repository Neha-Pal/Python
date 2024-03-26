n = int(input("Enter the value of n: "))
sum = 0
sign = -1
for i in range(1,n+1):
    sign = sign * -1
    sum = sum + sign * 1/i
print("Sum of series for first",n,"terms is",sum)