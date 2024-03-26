string = input('Enter a string: ')
lower = upper = digit = space = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == ' ':
        space += 1

print('The number of uppercase letters:', upper)
print('The number of lowercase letters:', lower)
print('The number of digits:', digit)
print('The number of whitespace characters:', space)