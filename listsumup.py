#	 To find the pair of numbers that sum up to given value

A = [1, 0, 2, 5, 7, 8]
n = 3
s = set()

for i in range(len(A)):
	temp = n - A[i]
	if (temp in s):
		print("("+str(A[i])+","+str(temp)+")")
	s.add(A[i])
