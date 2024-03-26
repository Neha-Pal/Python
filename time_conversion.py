s=int(input("enter time in second:"))
h=s/3600
print("hours:", h)
s=s%3600
m=s/60
print("minutes:", m)
s=s%60
print("seconds:",s)