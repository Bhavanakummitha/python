st=input('Enter  the string:')
char=input('Enter character you want:')
count=0
for i in st:
    if i==char:
        count+=1
        print(char,count)

