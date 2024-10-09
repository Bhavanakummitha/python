st='corepython@345'
alphacount=0
digitcount=0
splcharcount=0
for i in st:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        alphacount+=1
    elif i>='0' and i<='9':
        digitcount+=1
    else: 
       splcharcount+=1

       if alphacount>=1 and digitcount>=1 and splcharcount>=1 :
           print('perfect string')
       else:
           print('Not perfect string')

    
