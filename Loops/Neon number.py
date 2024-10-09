n=5
sqr=n**2
sum=0
while sqr>0:
    digit=sqr%10
    sum+=digit
    sqr//=10
if sum==n:
        print("Given number is neon number")
else:
        print("Not a neon number")
