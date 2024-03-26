
# to print numbers from 1 to 10 QS=1
for i in range(1, 11):
    print(i)


# To calculate the sum of all integers from 1 to number entered QS=2

num = int(input("Enter a positive number:"))
sum = 0
for i in range(1, num+1):
    sum = sum+i
print("sum of all numbers upto", num, "is:", sum)


# to print Multiplication Table QS=3

num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "X", i, "=", num*i)


# to find the factorial of a number QS=4
num = int(input("Enter a number:"))
if (num < 0):
    print("Please enter a valid number")
elif (num == 0):
    print(1)
else:
    factorial = 1
while (num > 0):
    factorial = factorial*num
    num = num-1
print("The factorial of", num, "is:", factorial)


# To find the value of one number raised to the power of another QS=5

num = int(input("Enter a number:"))
pow = int(input("Enter the power of the number:"))
ans = num**pow
print("The final answer is:", ans)


# Reverse of a number QS=6

num = int(input("Enter the number:"))
temp = num
rev_no = 0
while (temp > 0):
    digit = temp % 10
    rev_no = digit+rev_no*10
    temp = int(temp/10)
print("Reverse of", num, "is:", rev_no)


# To display the sum of digits of a number QS=7

num = int(input("Enter a number:"))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum+digit
    temp = int(temp/10)
print("Sum of digits of ", num, "is:", sum)


# To determine if a number is palindrome or not QS=8

num = int(input("Enter a positive integer: "))
temp = num
rev_no = 0
while temp > 0:
    digit = temp % 10
    rev_no = digit + rev_no*10
    temp = int(temp/10)
if num == rev_no:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


# To display the binary equivalent of a decimal inteher QS=9

num = int(input("Enter a Decimal number:"))
binary = 0
place = 1
n = num
while (n > 0):
    r = int(n % 2)
    binary = binary+r*place
    place = place*10
    n = n/2
print("Binary representation of", num, "is:", binary)


# To display the decimal equivalent of a binary inteher QS=10

binary = input("Enter a binary number: ")
decimal = 0
place = 0
for i in reversed(binary):
    decimal = decimal + int(i)*pow(2, place)
    place = place+1
print("Decimal representation of binary", binary, "is", decimal)


# To check whether a number is prime or not QS=11

num = int(input("Enter a number:"))
if (num > 1):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break
else:
    print(num, "is not a prime number")


# To display the GCD of two numbers QS=12

divisor = int(input("Enter 1st number:"))
dividend = int(input("Enter 2nd number:"))
rem = 1
while (rem != 0):
    rem = dividend % divisor
    if (rem == 0):
        HCF = divisor
    else:
        dividend = divisor
        divisor = rem
print("HCF is:", HCF)


# To display the positive ,negative and zeros that the user make as input QS=13

positive = negative = zero = 0
choice = 'y'
while choice == 'y' or choice == 'Y':
    num = int(input("Enter a number:"))
    if num == 0:
        zero = zero+1
    elif num > 0:
        positive = positive+1
    else:
        negative = negative+1
    choice = input("Do you wish to continue(Y/N)?:")
print("Positive Numbers :", positive,
      ",Negative Numbers :", negative, ",Zeros are:", zero)
