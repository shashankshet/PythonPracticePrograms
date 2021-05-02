#--------------------------------Kadane's algo/Max sub araay----------------------------------
n = int(input())
arr =list(int(num) for num in input().strip().split())[:n]
max_so_far = max_ending_here = 0
for i in range(0,n):
	max_ending_here = max_ending_here + arr[i]
	if (max_so_far < max_ending_here):
		max_so_far = max_ending_here
	if (max_ending_here<0):
		max_ending_here = 0
print(max_so_far)