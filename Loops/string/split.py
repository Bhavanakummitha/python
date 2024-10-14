#st='Hello Python Programming Language'
#s=st.split()
#for i in s:
      #if len(i)%2==1:
            #print(i)

#st=input('Enter the string:')
#s=st.split()
#max_len=0
#max_word=''
#for i in s:
      #if len(i)>max_len:
           # max_len=len(i)
            #max_word=i
#print('Longest word in the given string is:',max_word)


st=input('Enter the string:')
s=st.split()
min_len=len(st)
min_word=''
for i in s:
      if len(i)<min_len:
            min_len=len(i)
            min_word=i
print('shortest word in the given string is:',min_word)


