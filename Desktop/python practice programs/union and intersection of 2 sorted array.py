#6.-------------------------------------------------union and intersection of 2 sorted array-------------------------------

#Union

t = int(input())

while(t):
	n,m = input().split()
	arr = list(int(num) for num in input().strip().split())[:int(n)]
	arr1 = list(int(num) for num in input().strip().split())[:int(m)]
	res = arr+arr1
	a = set(res)
	print(len(a))
		
	t=t-1

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