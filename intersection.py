#intersection

arr=[1,2,3,4,5]
arr1=[1,2,3]
res=[]
if(len(arr)>len(arr1)):
	for i in range(0,len(arr1)):
		if(arr1[i] in arr):
			res.append(arr1[i])
	print(res)
else:
	for i in range(0,len(arr)):
		if(arr[i] in arr1):
			res.append(arr[i])
	print(res)