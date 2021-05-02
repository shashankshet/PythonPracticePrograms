#---------------------------------------------------Count pairs with given sum-------------------------------------------
n=int(input())
k=int(input())
arr =list(int(num) for num in input().strip().split())[:n]

def get_pairs_count(arr,n,k):
	count=0
	for i in range(n):
		for j in range(i+1,n):
			if(arr[i]+arr[j]==k):
				count+=1
	return count

print(get_pairs_count(arr,n,k))

