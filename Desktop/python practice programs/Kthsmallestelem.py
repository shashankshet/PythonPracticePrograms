#3. To find the kth smallest element in the array------------------------
t = int(input())

while(t):
	n = int(input())
	arr = list(int(num) for num in input().strip().split())[:n]
	k = int(input())
	arr = sorted(arr)
	print(arr[k-1])
	t=t-1