#----------------------------------Minimize the height-------------------------------------------
k = int(input())
n = int(input())
arr =list(int(num) for num in input().strip().split())[:n]
if(n==1):
	print(0)

arr.sort()

ans = arr[n-1] -arr[0]

small = arr[0] + k
big = arr[n-1] - k

if(small > big):
	small,big = big,small

for i in range(1,n-1):

	sub = arr[i] - k
	add = arr[i] + k

	if(sub >= small or add <= big):
		continue
	if(big - sub <= add - small):
		small = sub
	else:
		big = add
print(min(ans,big-small))


