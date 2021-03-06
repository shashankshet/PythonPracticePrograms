#4----------------------------------Sort 0 1 2 in an array-------------------------------------------
n = int(input())
arr = list(int(num) for num in input().strip().split())[:n]
arr = sorted(arr)
print(arr)
#4.=====================================alternate approach==================
# def sort012(arr,n):
#     # code here
#     lo = 0
#     hi = n - 1
#     mid = 0
#     while mid <= hi: 
#         if arr[mid] == 0: 
#             arr[lo], arr[mid] = arr[mid], arr[lo] 
#             lo = lo + 1
#             mid = mid + 1
#         elif arr[mid] == 1: 
#             mid = mid + 1
#         else: 
#             arr[mid], arr[hi] = arr[hi], arr[mid]  
#             hi = hi - 1
#     return arr