#Question 4
# Check if the string is pangram

def ispangram(str):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for char in alphabet:
		if char not in str.lower():
			return False

	return True
	
s=input("Enter a String: ")
if(ispangram(s) == True):
	print(f"Yes '{s}' is a panagram")
else:
	print(f"No '{s}' is not a panagram")
print()





