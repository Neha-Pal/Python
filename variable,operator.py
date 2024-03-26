
# Print your name QS->1

import math
name = input("Write your name:")
print("Hello", name)


# sum of two numbers QS->2

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum = a+b
print("The sum is:", sum)


# Temperature Conversion QS->3

C = float(input("Enter temperature in celcius:"))
F = 9/5*C+32
print("The temperature in Farenheit is:", F)


# Simple Interest QS->4

p = int(input("Enter principle:"))
r = float(input("Enter rate of interest:"))
t = int(input("Enter time:"))
simple_interest = p*t*r/100
print("Simple Interest is:", simple_interest)


# Time Conversion QS->5

s = int(input("Enter time in second:"))
h = s/3600
print("Hours:", h)
s = s % 3600
m = s/60
print("Minutes:", m)
s = s % 60
print("seconds:", s)


# Swap two variables using 3rd variable QS->6

a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = a
a = b
b = c
print("The 1st number is:", a)
print("The second number is:", b)


# Swap two variables without using 3rd variable QS->7

a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
a = a+b
b = a-b
a = a-b
print("The 1st number is:", a)
print("The second number is:", b)


# Circle_Area & Circumference QS->8

r = int(input("Enter radious of the circle:"))
area = math.pi*r*r
circumference = 2*math.pi*r
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)


# Rectangle_Area & Circumference QS->9

l = int(input("Enter the length of the rectangle:"))
w = int(input("Enter the width of the rectangle:"))
area = l*w
circumference = 2*(l+w)
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)


# Triangle_Area QS->10

s1 = float(input("Enter length of side 1: "))
s2 = float(input("Enter length of side 2: "))
s3 = float(input("Enter length of side 3: "))

s = (s1 + s2 + s3)/2
area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))

print("Area of triangle is ", area)


# Compound_Interest QS->11
p = int(input("Enter principle:"))
t = int(input("Enter time:"))
r = float(input("Enter rate of interest:"))
C = p*(1+r/100)**t-p
print("The compound interest is:", C)
