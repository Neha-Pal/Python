call=int(input("enter number of calls:"))
if call==100:
    charge=200

elif call>100 & call<=150:
    call=call-100
    charge=200+(0.60*call)
    
elif call>150 & call<200:
    call=call-150
    charge=200+(0.60*50)+(0.50*call)
else:
    call=call-200
    charge=200+(0.60*50)+(0.50*50)+(0.40*call)
print("the total charge is",charge,"rs")

