#Question 8
#Print all triplets within an array whose sum is zero

def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
			
# If no triplet with 0 sum found in array
	if (found == False):
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))