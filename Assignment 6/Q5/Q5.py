#Question 5
#Hyphen Seperated Sentence


input_string=str(input("Enter a hyphen separated sentence: "))

li=input_string.split("-") #Splitting the string into a list of strings
li.sort() #Sorting the list using sort function

print("-".join(li))
print()