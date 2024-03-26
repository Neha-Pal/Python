divisor = int(input("Enter first number: "))
dividend = int(input("Enter second number: "))
rem = 1

while rem!=0:
    rem = dividend % divisor
    if rem == 0:
        hcf = divisor
    else:
        dividend = divisor
        divisor = rem

print("HCF is", hcf)