side_1 = 0  # Variable to store first side of triangle
side_2 = 0  # Variable to store second side of triangle
side_3 = 0  # Variable to store third side of triangle

# Variables to store sum of two sides
sum_1 = 0
sum_2 = 0
sum_3 = 0

side_1 = int(input("Enter First side of the Triangle "))  # Take first side as input form user
side_2 = int(input("Enter Second side of the Triangle "))  # Take second side as input form user
side_3 = int(input("Enter Third side of the Triangle "))  # Take third side as input form user

# Calculate sum of sides taken 2 at a time
sum_1 = side_2 + side_3
sum_2 = side_1 + side_3
sum_3 = side_1 + side_2

if (sum_1 > side_1) & (sum_2 > side_2) & (sum_3 > side_3):  # Check if sum of sides is greater than third side
    print("Yes")                                            # if so print "Yes"
else:
    print("No")                                             # print "No"
