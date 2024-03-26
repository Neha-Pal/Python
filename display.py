text = 'SHIFT'
for i in range(0,6):
    newtext = text[i:] + text[:i]
    print(newtext)