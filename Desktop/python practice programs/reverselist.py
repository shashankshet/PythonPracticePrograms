def ReverseList(a,start,end):
	while start < end :
		a[start],a[end] =a[end],a[start]
		start+=1
		end-=1
a=[1,2,3,4,5,6]
print(a)
ReverseList(a,0,5)
print(a)