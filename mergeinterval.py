#--------------------------Merge intervals--------------------------------------
intervals=[[1,3],[2,6],[8,10],[15,18]]

def merger(arr):

	res = []
	for interval in sorted(intervals, key= lambda x:x[0]):
		if(res and  interval[0] <= res[-1][1]):
			res[-1][1]=max(res[-1][1],interval[1])
		else:
			res.append(interval)

	return res

print(merger(intervals))
        