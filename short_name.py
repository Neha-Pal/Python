name=input('enter your name:')
s1=name.find(' ')
s2=name.find(' ',s1+1)
#short=name[0]+'.'+name(s1+1)+'.'+name(s2+1)+'.'
short = name[0] +'. '  + name[s1+1] +'. ' + name[s2+1] +'.'
print('short form:',short)
