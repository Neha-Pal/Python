string = input("Enter a string : ")
new_string = string[-1:] + string[1:-1] + string[:1]
print(new_string)