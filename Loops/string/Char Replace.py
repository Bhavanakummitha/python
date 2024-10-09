st='m d m'
res=''
char=input('Enter the character you want to  replace:')
for i in st:
 if i=='':
     i=char
     res+=i
 print('updated string is:',res)
