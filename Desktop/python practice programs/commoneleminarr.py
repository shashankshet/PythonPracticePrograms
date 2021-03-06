#-----------------------Commaon elements in 3 arrays---------------------------------------------------
A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]
n1=6
n2=5
n3=8
res=[]

s= set(A).intersection(set(B),set(C))
s=list(s)
s=sorted(s)
print(s)