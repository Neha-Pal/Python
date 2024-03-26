sum = 0
fact = 1
for i in range(1,8):
    fact= fact*i
    sum= sum + i/fact
print("Sum of series is",sum)