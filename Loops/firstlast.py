n=int(input()) 
ld=n%10
fd=0
while n>0:
    digit=n%10
    fd=digit
    n//=10
print('first digit is:',fd)
print('last digit is:',ld)
print('sum of fd and ld is:',fd+ld)
    