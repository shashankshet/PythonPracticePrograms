#---------------------Pallindrome---------------------------------------------
msg= input()
msg1= msg[::-1]
if(msg==msg1):
	print("Pallindrome")
else:
	print("Not a Pallindrome")

string = input()
dup = {}
for i in string:
	if i in dup:
		dup[i]+=1
	else:
		dup[i]=1
print(str(dup))

def ReverseList(a,start,end):
	while start < end :
		a[start],a[end] =a[end],a[start]
		start+=1
		end-=1
a=[1,2,3,4,5,6]
print(a)
ReverseList(a,0,5)
print(a)