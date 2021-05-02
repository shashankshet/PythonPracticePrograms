#-------------------------------Find factorial of a large number--------------------------------
def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*factorial(n-1)
t = int(input())
while(t):
	n = int(input())
	print(factorial(n))
	t=t-1