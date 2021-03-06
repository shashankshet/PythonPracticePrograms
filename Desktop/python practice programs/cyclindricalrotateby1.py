
#----------------------------Cylindrically rotate an array by 1--------------------------------------
t = int(input())

while(t):
    n = int(input())
    a = list(int(num) for num in input().strip().split())[:n]
    arr= [a[-1]] + a[0:-1]
    print(*arr, sep=' ')
    
    t=t-1