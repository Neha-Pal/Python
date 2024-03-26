
# To determine the smallest and largest number amnog the user input QS=14
import random
min = 9999
max = 0
choice = 'y'
while choice == 'y' or choice == 'Y':
    num = int(input("Enter a number:"))
    if (num > max):
        max = num
    elif (num < min):
        min = num
    choice = input("Do you wish to continue(Y/N)?:")
print("Maximum number:", max, "\nMinimum number:", min)


# An armstrong number of three digits is an integer such that the sum of the cobes of its digits are equal to the number QS=15
number = 0
sum = 0
for i in range(0, 1000):
    number = i
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum+pow(digit, 3)
        number = int(number/10)
    if i == sum:
        print(i)


# Fibonacci series QS=15
num = int(input("Enter a number:"))
n1 = n3 = 0
n2 = 1
print(n1, n2, end=" ")
for i in range(3, num+1):
    n3 = n1+n2
    print(n3, end=" ")
    n1 = n2n2 = n3


# series{(1/1!)+(2/2!)+......} QS=16
sum = 0
fact = 1
for i in range(1, 8):
    fact = fact*i
    sum = sum+i/fact
print("Sum of series is:", sum)


# series{1-(1/2)+(1/3)-(1/4)+...} QS=17
n = int(input("Enter the value of n:"))
sum = 0
sign = -1
for i in range(1, n+1):
    sign = sign*-1
    sum = sum+sign*1/i
print("Sum of series for first", n, "terms is:", sum)


# pattern 1 QS=18
'''
*********
*********
*********
*********
*********
'''

for i in range(4):
    for j in range(10):
        print("*", end=' ')
    print()


# Pattern 2 QS=19
'''
*
**
***
****
*****
'''

for i in range(1, 6):
    for j in range(5, i-1):
        print(" ", end=' ')
    for k in range(1, i+1):
        print("*", end=" ")
    print()


# Pattern 3 QS=20
'''
      *
     **
    ***  
   ****
'''

for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end='')
    for k in range(1, i+1):
        print("*", end='')
    print()


# Pattren 4 QS=21
'''
       *
      ***
     *****
'''

for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end='')
    for k in range(1, 2*i):
        print("*", end='')
    print()


# Pattern 5 QS=22
'''
   1
  222
 33333
4444444
'''

for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end='')
    for k in range(1, 2*i):
        print(i, end='')
    print()


# Pattern 6 QS=23
'''
   1
  212
 32123
4321234
'''

for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end='')
    for k in range(i, 0, -1):
        print(k, end='')
    for l in range(2, i+1):
        print(l, end='')
    print()


# Floyd's Triangle QS=24
'''
1
2 3
4 5 6
7 8 9 10
'''

k = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(k, end=' ')
        k = k+1
    print()


# Write a program to compute sin x for given x. sin x = x - x3/3! + x5/5! - x7/7! + x9/9! .......QS=25
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sign = -1
fact = i = 1
sum = 0
while i <= n:
    p = 1
    fact = 1
    for j in range(1, i+1):
        p = p*x
        fact = fact*j
    sign = -1*sign
    sum = sum + sign * p/fact
    i = i+2
print("sin(", x, ") =", sum)


# Write a program to compute cosine of x. cos x = 1 - x2/2! + x4/4! - x6/6! ...QS=26

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sign = -1
fact = 1
i = 2
sum = 0
while i <= n:
    p = 1
    fact = 1
    for j in range(1, i+1):
        p = p*x
        fact = fact*j
    sum = sum + sign * p/fact
    sign = -1*sign
    i = i+2
print("cos(", x, ") =", 1+sum)


# GUESSING GAME QS=27


computer = random.randint(1, 100)
player = 0
tries = 0

print("Guess My Number Game")

while (player != computer):
    player = int(input('Enter your guess: '))
    tries = tries + 1

    if player < computer:
        print('Too low, try again.')
    elif player > computer:
        print('Too high, try again.')
    else:
        print("Correct!,you got it in", tries, "tries")
