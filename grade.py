a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
avarage=(a+b+c)/3
if 100>=avarage and avarage>=90:
    print("the grade is A")
elif 89>=avarage and avarage>=80:
    print("the grade is B")
elif 79>=avarage and avarage>=70:
    print("the grade is C")
elif 69>=avarage and avarage>60:
    print("the grade is D")
elif avarage>=59:
    print("the grade is F")
