upper=lower=digit=length=False
password=input("enter a strong password:")
if len(password)>=8:
    length=True
    for letter in password:
        if letter.isupper():
            upper=True
        elif letter.islower():
            lower=True
        elif letter.isdigit():
            digit=True
if length and upper and lower and digit:
    print("It is a valid password")
else:
    print("It is not a valid password")
