positive=negative=zero=0
choice = 'Y'
while choice=='y'or choice=='Y':
    num = int(input("Enter a number: "))
    if num==0:
        zero=zero+1
    elif num>0:
        positive=positive+1
    else:
        negative=negative+1

    choice=input("Do you wish to continue(Y,N)?: ")
	
print("Positive numbers:",positive,", Negative numbers:",negative,", Zeros:",zero)
