st='Bhavanareddy'
res1=''
res2=''
for i in range(len(st)//2,len(st)):
    res1=st[i]+res1
for i in range(len(st)//2):
    res2+=st[i]
print('upadted string is:',res2+res1)



#reverse string of given string:
st='abcde46'
alpha=''
digit=''
for i in st:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        aplha=i+alpha
    elif i>='0' and i<='9':
        digit=i+digit
        print('updated string:',alpha+digit)