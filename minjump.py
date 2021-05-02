#------------------------------min jump to reach the end of the array-------------------------------------------

n = int(input())
arr = list(int(num) for num in input().strip().split())[:n]
jump=0
if(arr[0]==0):
	print("cannot reach the end")
if(arr[0]==arr[n-1]):
	jump = jump+1
	print(jump)
if(arr[n-1] in arr[1:n-1]):
		jump = 3
		print(jump)
else:
	jump=jump+2
	print(jump)