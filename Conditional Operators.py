
# Even/Odd QS->1

import math
n = int(input("Enter a Number:"))
if n % 2 == 0:
    print("The number", n, "is Even")
else:
    print("The number", n, "is Odd")


# Define the large number among two 2 umbers QS->2

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if (a > b):
    print("the number", a, "is greatest")
else:
    print("the number", b, "is greatest")


# Define the large number among two 3 umbers QS->3

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if (a > b):
    if (a > c):
        print(a, "is greatest")
    else:
        print(c, "is greatest")
elif (b > c):
    print(b, "is greatest")
else:
    print(c, "is greatest")


# Leap year/not QS->4
y = int(input("Enter year:"))
if (y % 400 == 0):
    print(y, "is leap year")
elif (y % 100 == 0):
    print(y, "is not a leap year")
elif (y % 4 == 0):
    print(y, "is a leapyear")
else:
    print(y, "is not a leap year")


# Telephone_bills QS->5

call = int(input("enter number of calls:"))
if (call == 100):
    charge = 200
elif (call > 100 & call <= 150):
    call = call-100
    charge = 200+(0.60*call)
elif (call > 150 & call < 200):
    call = call-150
    charge = 200+(.60*50)+(0.50*call)
else:
    call = call-200
    charge = 200+(0.60*50)+(0.50*50)+(0.40*call)
print("The total charge is:", charge, "rs")


# To determine the roots of the quadratic equation QS->6

a = float(input("enter coefficient of a:"))
b = float(input("enter coefficient of b:"))
c = float(input("enter coefficient of c:"))
d = (b**b)-4*a*c
D = math.sqrt(d)
if (d == 0):
    print("The equation has two equal roots")
elif (d > 0):
    print("The equation has two real roots")
elif (d < 0):
    print("The equation has two complex roots")
print("The roots are:\n")
r1 = (-b-D)/2*a
r2 = (-b+D)/2*a
print(r1, "\n")
print(r2, "\n")


# Grade of a student QS->7

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("enter 3rd number:"))
avg = (a+b+c)/3
if (100 >= avg >= 90):
    print("Grade is A")
elif (89 >= avg >= 80):
    print("Grade is B")
elif (79 >= avg >= 70):
    print("Grade is C")
elif (69 >= avg >= 60):
    print("Grade is D")
else:
    print("FAIL")


# Print days QS->8

day = int(input("Enter the day:"))
if (day == 1):
    print("Sunday")
if (day == 2):
    print("Monday")
if (day == 3):
    print("Tuesday")
if (day == 4):
    print("Wednesday")
if (day == 5):
    print("Thursday")
if (day == 6):
    print("Friday")
if (day == 7):
    print("Saturday")


# Vowel/Consonant QS->9

ch = input("Enter a alphabet:")
if (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print("The alphabet ", ch, "is Vowel")
else:
    print("The alphabet", ch, "is Consonant")
