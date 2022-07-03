#Question 2
#Palindrome String

def palindrome(s):
    s1=""
    s1 = s[::-1]
    return s1
S=input("Enter a String: ")
if(palindrome(S)==S):
    print(S,"is a palindrome")
else:
    print(S,"is not a palindrome") 
print()
