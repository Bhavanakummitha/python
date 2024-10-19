st='Language'
start=0
leng=int(input('enter the length of the substring:'))
while start<=len(st):
    end=start+1
    while end<=len(st):
        substring=st[start:end]
    if len(substring)==leng:
          print(substring)
    end+=1
    start+=1
    
        
