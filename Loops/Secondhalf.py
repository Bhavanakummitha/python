st='language'
res=''
for i in range(len(st)//2,len(st)):
    ch=st[i]
    res+=ch
print(res)

#duplicate values:
st='maximum'
res=''
for i in st:
    if i not in res:
     res+=i
     print(res)
#second half uppercase:
st='language'
res=''
for  i in range(len(st)//2,len(st)) and chr(ord(st)-32):
   res1=res1+i
   res=res(st)
   print(res)
   