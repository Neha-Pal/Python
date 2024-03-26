number=0
sum=0
for i in range(0,1000):
    number=i
    sum=0
    while number>0:
        digit = number%10
        sum=sum+pow(digit,3)
        number= int(number/10)
    if i==sum:
        print(i)