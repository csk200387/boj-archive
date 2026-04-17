import sys
import heapq
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline().strip()))
for i in range(0,n):
    print(heapq.heappop(arr))