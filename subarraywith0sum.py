#---------------------------------Subarray with zero sum=--------------------------------------------------------------
#!!!!!!!!!!!!!!this approch fails due to n**2 time complexity
def subarray(arr,n):
	n_sum=0
	s=set()
	for i in range(n):
		n_sum+=arr[i]

		if n_sum==0 or n_sum in s:
			return True
		s.add(n_sum)
	return False

arr=[-3,2,1,6,3]
n=len(arr)
if subarray(arr,n):
	print('Yes')
else:
	print('No')
