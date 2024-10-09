st='212.321`,456.898'
res=''
for i in st:
    if i==',':
        i='.'
    elif i=='.':
        i=','
        res+=i
print(res)

