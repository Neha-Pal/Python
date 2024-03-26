'''
# vowel /consonant QS 1
ch = input("enter a alphabet:")
if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
    print("the alphabet ", ch, "is a vowel")
else:
    print("the alphabet ", ch, "is a consonant")

'''
# uppercase/lowercase/digits QS 2

text = input('Enter a string: ')
lower = upper = digit = space = 0

for ch in text:
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

'''
# to exchange 1st and last characters QS 3

text = input('Enter a string: ')
newtext = text[-1]+text[1:-1]+text[0]
print('New string:', newtext)


# to inverse a string QS 4
text = input('Enter a string: ')
newtext = ''
for ch in text:
    newtext = ch + newtext
print('New string:', newtext)


# to shift one position to left QS 5

text = input('Enter a string: ')
newtext = text[1:] + text[0]
print('New string:', newtext)


# full name to short form QS 6

text = input('Enter a string: ')

space1 = text.find(' ')

space2 = text.find(' ', space1+1)
newtext = text[0] + '. ' + text[space1+1] + '. ' + text[space2+1] + '.'
print('New string:', newtext)


# to check a string is palindrome or not QS 7

text = input('Enter a string: ')

newtext = text[::-1]

if text == newtext:
    print('String is palindrome')
else:
    print('String is not palindrome')



# shift
# hifts
# iftsh
# ... QS 8


text = 'SHIFT'
for i in range(0, 6):
    newtext = text[i:] + text[:i]
    print(newtext)


# passwords QS 9

upper = lower = digit = length = False
password = input("enter a strong password:")
if len(password) >= 8:
    length = True
    for letter in password:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True
        elif letter.isdigit():
            digit = True
if length and upper and lower and digit:
    print("It is a valid password")
else:
    print("It is not a valid password")
'''