n=5602
n=int(input('Enter a number:'))
count=0
while n>0:
    digit=n%10
    count+=1
    n//=10
    print('count of digits is:',count)
