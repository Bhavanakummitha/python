n=int(input('Enter a number:'))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n//=10
    print('sum of digits is:',sum)
else:
    print('s')

    

    
