st='aabcdde'
i=0
res=''
while i<len(st)-1:
    ch1=st[i]
    ch2=st[i]
if ch1==ch2:
    res+=ch1
    i+=1
print(res)


st='aa3b2c1d'
res=''
for i in range(len(st)):
    ch1=st[i]
    ch2=st[i+1]
    if ch1>='a' and ch1<='z' and ch2>='0' and ch2<='9':
        res=res+ch1*int(ch2)
    if ch1>='a' and ch1<='z' and ch2>='a' and ch2<='z':
         res=res+ch1
    if st[-1]>='a' and st[-1]<='z':
        res+=st[-1]
    print(res)

