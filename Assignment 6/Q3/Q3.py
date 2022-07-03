#Question 3
#Pascal's Triangle

def factorial(m):
    s=1
    for i in range(1,m+1):
        s*=i
    return s

def pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            #nCr=n!/(r!(n-r)!)
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
        
        print() #Printing new line
N=int(input("Enter a number: "))
pascal(N)
print()


