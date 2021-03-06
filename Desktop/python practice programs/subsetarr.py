#------------------------------Array subset of another array-------------------------------------
t=int(input())
while(t):
	m,n=map(int,input().split())
	arr1=list(int(num) for num in input().strip().split())[:m]
	arr2=list(int(num) for num in input().strip().split())[:n]
	a=set(arr1)
	b=set(arr2)
	z = b.issubset(a)
	if(z):
		print("Yes")
	else:
		print("No")
	t=t-1 