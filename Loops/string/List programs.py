#count of elements:
l=[2,3,4,5,6,7]
count=0
for i in l:
      count+=1
      print(count)
#range:
l=[2,3,4,5,6,7]
count=0
for i in range(len(l)):
      count+=1
      print(count)
 #even element count:
l=[2,3,4,5,6,7,8,9,10]
count=0
for i in l:
      if i%2==0:
            count+=1
            print(count)
            
#count of even and odd elements:
l=[2,3,4,5,6,7,8,9,10]
count1=0
count2=0
for i in l:
      if i%2==0:
            count1+=1
      else:
            count2+=1
      print('count of the even elements:',count1)
      print('count of the odd elements:',count2)
#odd indexed elements:
l=[2,3,4,5,6,7,8,9]
for i in range(len(l)):
      if i%2==1:
            print(l[i])
#even indexed elements:
l=[2,3,4,5,6,7,8,9]
for i in range(len(l)):
      if i%2==0:
            print(l[i])
#even and odd indexed elements:
l=[2,3,4,5,6,7,8,9]
c1=0
c2=0
for i in range (len(l)):
      if i%2==0:
            c1+=1
      else:
            c2+=1
            print(c1,c2)
#largest element:
l=[2,3,4,5,6,7,8,9]
lrg=0
for i in l:
      if i>lrg:
            lrg=i
      print(lrg)

#smallest element:
l=[2,3,4,5,6,7,8,9]
sml=l[0]
for i in l:
      if i<sml:
            sml=i
      print(sml)

