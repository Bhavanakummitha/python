from collections import Counter
def max_occurred_char(input_string):
    
    char_count = Counter(input_string)
    

    max_char = max(char_count, key=char_count.get)
    
    return max_char, char_count[max_char]

st='abbccc'
def min_occurred_char(st):
    
    freq = Counter(st)
    

    min_char = min(freq, key=freq.get)
    
    return min_char, freq[min_char]
 
 #question 3:
st=input('enter the reverse input:')
res=''
for i in st:
    if i>='0' and i<='9':
        print(i)
        res=res+i
        print(res)

st='aaabbc'
def compress_string(s):
    
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
      
            result += s[i - 1] + str(count)
            

    result += s[-1] + str(count)
    input='aaabbc'
    return result
print(res)


#question 4:
from collections import Counter

def second_most_frequent_char(s):
    
    char_count = Counter(s)
    
    
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    if len(sorted_chars) < 2:
        return None
    
    
    return sorted_chars[1][0]

string = "successes"
result = second_most_frequent_char(string)

if result:
    print(f"The second most frequent character is: {result}")
else:
    print("No second most frequent character found.")


# minimum occured character:
st='aaabbc'
def compress_string(s):
    #st="aaabbc"
    #res= ""
    #count = 1
    #for i in range(1, len(s)):
        #if s[i]<min(len(i)):
           # count+= 1
        #else:
            #c+=1
            #print(res)
 st="aaabbc"
res=''
def min_occurred_char(st):
    
    freq = Counter(st)
    

    min_char = min(freq, key=freq.get)
    
    return min_char, freq[min_char]
  
#minimum occured character:
st='aaabbc' 
res='' 







        

