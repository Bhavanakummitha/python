n=int(input('Enter the number'))
sum=0
prod=1
while n>0:
    digit=n%10
    sum+=digit
    prod*=digit
    n//=10
if sum==prod:
    print('Spy number')
else:
    print('Not a Spy number')
