#--------------------merging 2 arrays without using extra space------------------------------
arr1 = [1,3,5,7]
arr(2 = [2,4,6,8]

print(*sorted(arr1+arr2), sep=' ')

#--------------------------Merge intervals--------------------------------------
# intervals=[[1,3],[2,6],[8,10],[15,18]]

# def merger(arr):

# 	res = []
# 	for interval in sorted(intervals, key= lambda x:x[0]):
# 		if(res and  interval[0] <= res[-1][1]):
# 			res[-1][1]=max(res[-1][1],interval[1])
# 		else:
# 			res.append(interval)

# 	return res

# print(merger(intervals))