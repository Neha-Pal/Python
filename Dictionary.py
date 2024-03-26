
# to convert the unique words of the string into lowercase QS 1

import time
a = input("enter your strings:")
b = set(a.split())
unique = set(b)
print("Here the unique words are:", unique)
print("Lowercase:", a.lower())


# to convert all input in lowercase  and count digits,spaces and all QS 2

a = input("Enter a string:")


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(char_frequency(a))


# vowel to special character QS 3
a = input("Enter a strings:")
a = a.lower()
c = a.replace("a", "#").replace("e", "@").replace("i",
                                                  "$").replace("o", "%").replace("u", "!")
print(f"The alphabet is:{a} and the replace value is:{c}")


# to print the common word among two strings QS 4

a = input("Enter the 1st string:")
b = input("Enter the 2nd string:")
c = list(set(a) & set(b))
print("The common letters are:")
for i in c:
    print(i)

# to print the no of students QS 5

students = {}
n = int(input("enter the no of students:"))
for i in range(n):
    sname = input("Enter the student name:")
    marks = []
    for j in range(5):
        marks = int(input("enter the marks:"))
        marks.append(marks)
    students[sname] = marks
print(students)


# name_game QS 6

print("let's start agame...")
Birthdays = {
    "Arpa": "23/9/2013",
    "Shumbham": "4/10/2011",
    "Anurag": "9/8/2015",
    "Shubhayan": "7/2/1200",
}
print("Welcome to birthday game!...")
time.sleep(0.1)
for x in Birthdays:
    print(x)
    time.sleep(0.7)
choice = input("Who's birthday do you want to look?")
if choice in Birthdays:
    print("Birthday of", format(choice), "is:")
    print(Birthdays[choice])
