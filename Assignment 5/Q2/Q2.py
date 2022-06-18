# Asking user for Inputs:
lowerrange = int(input('Enter lower range: '))
upperrange = int(input('Enter upper range: '))
n = int(input('Enter number to check for: '))

numbers=''

for i in range(lowerrange,upperrange+1):
    if i%n == 0:
        numbers = numbers + ', ' + str(i)

# We are slicing the answer string because there's an additional ", " at the start
print('The numbers are:', numbers[2::])
