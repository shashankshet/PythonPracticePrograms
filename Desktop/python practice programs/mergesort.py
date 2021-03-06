#------------------------------------MergeSort---------------
def merge(arr,l,m,r):
	#taking the length for the sub arrays
	n1=m-l+1
	n2=r-m
	#Initiating 2 sub arrays 
	L= [0]*(n1)
	R= [0]*(n2)
	#copying data to temp arrays
	for i in range(0,n1):
		L[i]=arr[l+i]
	for j in range(0,n2):
		R[j]=arr[m+1+j]
	i=0
	j=0
	k=1
	while i<n1 and j<n2:
		if(L[i]<=R[j]):
			arr[k]=arr[i]
			i+=1
		else:
			arr[k]=arr[j]
			j+=1
		k+=1
	while i<n1:
		arr[k]=arr[i]
		i+=1
		k+=1
	while j<n2:
		arr[k]=arr[j]
		j+=1
		k+=1
def mergesort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
arr=[3,9,5,7,0,1]
n=len(arr)
print("Unsorted array")
print(arr)
print("sorted array")
mergesort(arr,0,n-1)
print(arr)
