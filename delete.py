text = input('Enter a string: ')
words = text.split()

data = input('Enter a word to delete: ')
status = False

for word in words:
    if word == data:
        words.remove(word)
        status = True

if status:
    text = ' '.join(words)
    print('String after deletion:',text)
else:
    print('Word not present in string.')