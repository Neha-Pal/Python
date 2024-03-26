num = int(input("Enter a positive integer: "))
temp = num
rev_no=0
while temp>0:
    digit = temp%10
    rev_no= digit + rev_no*10
    temp= int(temp/10)
if num==rev_no:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")