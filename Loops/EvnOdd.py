n=int(input('Enter a number:'))
n=2657
prd=1
while n>0:
    digit=n%10
    if digit%2!=0:
        prd=prd*digit
   n//10
print('prd of odd digits is:',prod)
 if prod%2 ==0:
        print('Even prod')
 else:
        print('odd prd')