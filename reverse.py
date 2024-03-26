num = int(input("Enter a number: "))
temp = num
rev_no=0
while temp>0:
    digit = temp%10
    rev_no= digit + rev_no*10
    temp= int(temp/10)
print("Reverse of",num,"is",rev_no)