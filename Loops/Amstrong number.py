n=int(input())
n=153
n1=n
count=0
sum=0
while n>0:
 digit1=n%10
 count+=1
 n//=10
 while n1>0:
  digit2=n%10
  sum=sum+digit2
  n//=10
if sum==n1:
 print('Given number is armstrong number')
else:
 print('Not Armstrong number')
