#4----------------------------------Sort 0 1 2 in an array-------------------------------------------
n = int(input())
arr = list(int(num) for num in input().strip().split())[:n]
arr = sorted(arr)
print(arr)