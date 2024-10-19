#l=[3,4,5,6,7]
#l1=[]
#for i  in l:
      #l1=l1+[i]
#print(l1)

#  l=[5,6,7,2,8,9]
#l1=[]
#l2=[]
#for i in l:
      #l1=l1+[i]
#else:
     #l2=l2+[i]
#print(l1)
# print(l2)

l=[2,3,4,-8,-9-11]
l1=[]
l2=[]
#for i in l:
      #if i>0:
            #l1=l1+[i]
      #elif i<0:
            #l2+=[i]
      #print(l1)
      #print(l2)
#prime elements:
l=[3,2,4,5,6,7]
prime=[]
for i in l:
      c=0
      ch=i
      j=1
while j<=ch:
      if ch%j==0:
            c+=1
      j+=1
if c==2:
      prime+=[i]
print(prime)
   
#prime and non-prime:
l=[3,2,4,5,6,7]
prime=[]
prime2=[]
for i in l:
      c=0
      ch=i
      j=1
while j<=ch:
      if ch%j==0:
            c+=1
      j+=1
if c==2:
      prime+=[i]
else:
      prime2+=[i]
print(prime)
print(prime2)  
#reverse list:
l=[2,3,5,7]
rev=[]
for i in l:
      rev=[i]+rev
print(rev)
#first half list:
l=[3,4,5,6,7,8]
l1=[]
i=0
while i<len(l)//2:
      ele=l[i]
      l1+=[ele]
      i+=1
print(l1)
#duplicate elements:
l=[3,4,5,5,4,6]
l1=[]
for i in l:
      if i not in l1:
            l1=l1+[i]
            print(l1)
# Largest second half:
l=[3,4,5,6,7,8]
lrg=0
for i in  range(len(l)//2,len(l)):
      if l[i]>lrg:
            lrg=l[i]
      print(i)
# i/p:l=[2,4,3,5,6,7]
# o/p:[4,16,9,25,36,49]
l=[2,4,3,5,6,7]
l1=[]
for i in l:
      l1+=[i**2]
print(l1)

# i/p:l=[2,4,3,5,6,7]
# o/p:[4,16,9,5,6,7]
l1=[]
l2=[]
for i in range(len(l)//2):
      l1+=[l[i]**2]
for j in range (len(l)//2,len(l)):
      l2+=[l[j]]
print(l1+l2) 



