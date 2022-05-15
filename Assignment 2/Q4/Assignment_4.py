max = 0  # Variable to store value of greatest number
num_1 = 0  # Variable to store value of first number
num_2 = 0  # Variable to store value of second number
num_3 = 0  # Variable to store value of third number

num_1 = float(input("Enter first number "))  # Take input of first number from user
num_2 = float(input("Enter second number "))  # Take input of second number from user
num_3 = float(input("Enter third number "))  # Take input of third number from user

if num_1 > num_2:  # compare num_1 and num_2
    max = num_1    # if num_1 is greater assign it to max
else:
    max = num_2    # else assign num_2 to max

if num_3 > max:  # compare num_3 and max
    max = num_3  # if num_3 is greater assign it to max
else:
    max = max    # else max is the greatest number

print("Greatest number from " + str(num_1) + ", " + str(num_2) + ", " + str(num_3) +  " is " + str(max))  # print the greatest number
