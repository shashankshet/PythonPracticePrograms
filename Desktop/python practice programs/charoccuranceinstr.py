#-----------------------Character occurence in a string------------------------------------
test_str = input()
all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] +=1
	else:
		all_freq[i]=1
print(str(all_freq))

for i in all_freq:
	if all_freq[i].value()==1:
		print(all_freq[i])