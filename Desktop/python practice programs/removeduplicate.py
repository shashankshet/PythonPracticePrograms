#------------------Removing duplicate elements from list----------------------
arr= [1,2,2,3,3,3,4,4,6]
res=[]
print("Original list")
print(arr)
for i in arr:
	if i not in res:
		res.append(i)
print("list after removing duplicates")
print(res)