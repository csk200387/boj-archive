import sys
import heapq
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline().strip()))
res = 0
for i in range(0,n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    res += a+b
    heapq.heappush(arr,a+b)
print(res)