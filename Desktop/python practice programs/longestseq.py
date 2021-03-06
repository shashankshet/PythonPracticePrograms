#---------------------------Longest consecutive subsequnce-----------------------------
n=int(input())
arr= list(int(num) for num in input().strip().split())[:n]

ans=0
count=0
arr.sort()
v=[]
v.append(arr[0])
count=1
for i in range(n):
	if(i>0 and arr[i]== arr[i-1]+1):
		count+=1
print(count)