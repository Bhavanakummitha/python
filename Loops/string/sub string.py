#st=input("enter the string:")
#start=0
#while start<=len(st):
 #end=start+1
#while end<=len(st):
 #substring=st[start:end]
#print(substring)
#start+=1
#end+=1

# sub string:

def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substrings(input_str, min_length):
    n = len(input_str)
    palindromes = []
    i = 0
    
    while i < n:
        j = i + min_length + 1  
        while j <= n:
            substring = input_str[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
            j += 1
        i += 1
    
    return palindromes


input_string = "babad"
min_substring_length = 2
palindromes = find_palindromic_substrings(input_string, min_substring_length)
print("Palindromic substrings with length greater than", min_substring_length, "are:")
for palindrome in palindromes:
    print(palindrome)
