#5--------------------------------------moving all negative int to a side of the array----------------------------------------
arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr = sorted(arr)
print(arr)

#-------------------another approch----------------------------------------
# def rearrange(arr, n):
# 	j = 0
# 	for i in range(0,n):
# 		if(arr[i]<0):
# 			temp = arr[i]
# 			arr[i] = arr[j]
# 			arr[j] = temp
# 			j = j+1
# 	print(arr)

# arr= [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# n = len(arr)
# rearrange(arr,n)