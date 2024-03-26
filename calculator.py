# my calculator
first=input("enter 1st number")
second=input("enter 2nd number")
first=int(first)
second=int(second)
print("enter operator(+,_,*,/,%,//,**):")
operator=input("enter operator")
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
elif operator=="//":
    print(first//second)
elif operator=="**":
    print(first**second)
else:
    print("invalid operator")