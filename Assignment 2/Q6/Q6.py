# Get the value of a and b
a = int (input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
# Calculating xor of a and b
num = a ^ b
Count_flipped_bit = 0
# Counting Number of set bit present
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)

