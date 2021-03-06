string = input()
dup = {}
for i in string:
	if i in dup:
		dup[i]+=1
	else:
		dup[i]=1
print(str(dup))