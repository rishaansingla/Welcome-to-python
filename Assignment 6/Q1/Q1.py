#Question 1
#Perfect Number

def perfect_number(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i #Storing the sum of divisors excluding the number itself
    if(s==n):
        return True
    else:
        return False

N=int(input("Enter a number: ")) #taking user's input
if(perfect_number(N)==True):
    print(N," is a perfect number")
else:
    print(N," is not a perfect number")
print()
