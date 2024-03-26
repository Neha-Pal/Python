first=input("input 1st number")
second=input("input 2nd number")
third=input("input 3rd number")
first=int(first)
second=int(second)
third=int(third)
if(first>second):
    if(first>third):
        print(first, "is the greatest")
    else:
        print(third, "is the greatest")
elif(second>third):
    print(second ,"is the greatest")
else:
    print(third, "is the greatest")