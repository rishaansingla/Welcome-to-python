input_string = "Python is a case sensitive language"
leng = 0  # variable to store length of string
index_1 = 0  # variable to store index of "a case sensitive language"
index_2 = 0  # variable to store index of "a"

leng = len(input_string)  # find length of string
print("Length of entered string is : " + str(leng) + "\n")  # print length of string

print("String after being reversed is : " + input_string[::-1] + "\n")  # reverse the string and print it

index_1 = input_string.find("a case sensitive language")  # find index of "a case sensitive language"
new_string = input_string[index_1:]  #  assign "a case sensitive language" to a new variable
print(new_string + " has been assigned to \"new_string\" \n")  # print the new variable

input_string = input_string[0:(index_1 + 1)] + " Object Orient Language"  # replace "case sensitive language" with "Object orient language"
print("String has been changed to : " + input_string + "\n")  # print it

index_2 = input_string.find("a")  # find index of "a"
print("Index of \"a\" is " + str(index_2) + "\n")  #print it

print("Here is the string after removing white spaces : " + input_string.strip())  # remove the white spaces and print them
