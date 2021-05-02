#----------------------------------median of 2 arrays of different size------------------------
import statistics
arr1=[2, 3, 5, 8]
arr2=[10, 12, 14, 16, 18, 20]
arr=arr1+arr2
arr=set(arr)
arr=list(arr)
print(int(statistics.median(arr)))

