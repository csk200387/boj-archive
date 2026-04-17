import heapq
import sys
input = sys.stdin.readline
heap = []
num = int(input().rstrip())
for i in range(num) :
    tmp = input().rstrip()
    heapq.heappush(heap, tmp)
for i in range(num) :
    tmp = heapq.heappop(heap)
    print(tmp)