n=int(input('Enter a number:'))
n=2657
sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        sum+=digit
    n//=10
    print(sum)
