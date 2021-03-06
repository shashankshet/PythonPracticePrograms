#-------------------------------median----------------------
import statistics
n=int(input())
arr=list(int(num) for num in input().strip().split())[:n]

print(int(statistics.median(arr)))