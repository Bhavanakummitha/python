i=10
sum=0
j=1
while i<=25:
    if i%2==1 and j<=4:
        sum+=i
        j+=1
    i+=1
print(sum)