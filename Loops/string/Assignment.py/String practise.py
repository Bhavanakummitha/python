st='hello world 123 haii'
res=''
for i in st:
      if i in 'aeiou' or i>='0' and i<='9':
            print(i)
            res=res+i
            print(res)

#question2:
st='hello world 123 haii' 
res='' 
for i in st:
      if i in 'aei ou' or i>='0' and i<='9':
            print(i)
            res=res+i
            print (res)

#question3:
st='hello world 123 haii'
res=''
for i in st:
      if i in 'aei ou':
            print(i)
            res=res+i
      print(res)

 #question 4:
st='hello world 123 haii'
res=''
for i in st:
      if i in i>='a' and i<='z':
            print(i)
            res=res+i
            print(res)

#question 5:
st='hello world' 
res='' 
for i in st:
      if i not in 'aeiouAEIOU':
             print(res)
      if i in 'aeiou':
            print(i)
            res=res+i
            print(res)
#question 6:
st='12hello3 4world4'
res=''
for i in st:
      if i in i>='a' and i<='z' and i>='0' and i<='9' or 'aeiou':
            print(i)
            res=res+i
            print(res)

#question 7:
st='12hello3 4world4'
res=''
for i in st:
  if i in i>='a' and i<='z':
      res=res+i
  if i in i>='0' and i<='9':
            print(i)
            res=res+i
            print(res)
#question 8:
st= '*12hello3$4#world'
res=''
letters = []
digits = []
special_chars = []

for char in st:
    if char.isalpha():  
        letters.append(char)
    elif char.isdigit():  
        digits.append(char)
    else:  
        special_chars.append(char)

letters_string = ''.join(letters)
digits_string = ''.join(digits)
special_chars_string = ''.join(special_chars)
print("Letters:", letters_string)
print("Digits:", digits_string)
print("Special characters:", special_chars_string)

#question 9:


            
            
            
            
            





               
