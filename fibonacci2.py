num = int(input("Enter no. of terms required: "))
n1=n3=0
n2=1
print(n1,n2,end=' ')
for i in range(3,num+1):
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3