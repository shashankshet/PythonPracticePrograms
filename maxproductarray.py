#-------------------------------MAximum product subarray-----------------------------
n = int(input())
arr = list(int(num) for num in input().strip().split())[:n]
res =arr[0]
for i in range(n):
	mul =arr[i]
	for j in range(i+1,n):
		res = max(res,mul)
		mul*=arr[j]

	res=max(res,mul)
print(res)