#---------------------returning the repeated element-----------------------------------------------------------
arr=[1,3,5,7,84,2,2]
arr.sort()
for i in range(len(arr)):
	if(arr[i]==arr[i-1]):
		print(arr[i])