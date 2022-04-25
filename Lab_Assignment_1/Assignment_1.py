#assignment 1
#question 1
print("enter three number to find their average")
num_1=float(input())
num_2=float(input())
num_3=float(input())
print((num_1+num_2+num_3)/3)


#question 2
gross_income=float(input("enter your gross income"))
standard_deduction=10000
dependent_deduction=3000
dependent_number=int(input("enter number of dependents"))
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependent_number)
rate=20/100
tax=taxable_income*rate
print("your income tax is",tax)



#question 3
lst=[12345678, "Raman Narayan", 'M', 'Cse', 9.2]
print(lst)


#question 4
lst=[]
for i in range(0,5):
    print("enter marks of student",i+1)
    lst.append(float(input()))
lst.sort()
print(lst)


#question 5a
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)
#question 5b
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print(color)
