n=int(input())
i=1
sum=0
while i<=n:
    sum*=i
    i+=1
    print(sum)

    n=int(input())
    while n>0:
        i=1
        sum=0
        while n>=i:
            digit=n%10
            sum=digit*i
            sum=i+1
            n//=10
    print(sum)
            
