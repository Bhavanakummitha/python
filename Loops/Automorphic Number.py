n=76
sqr=n**2
sum=0
while sqr>0:
    digit=sqr%10
    sum+=digit
    sqr//=10
if sum==n:
        print("Given number is Automorphic Number")
else:
        print("Not a Automorphic number")
