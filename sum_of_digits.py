num = int(input("Enter a positive integer: "))
temp = num
sum=0
while temp>0:
    digit = temp%10
    sum=sum+digit
    temp= int(temp/10)
print("Sum of digits of",num,"is",sum)
