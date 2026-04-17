import heapq
import sys
def ran(n):
    i = 1
    while i <= n:
        yield i
        i += 1
input = lambda:sys.stdin.readline().rstrip()
heap = []
num = int(input())
for i in ran(num) :
    tmp = input()
    heapq.heappush(heap, tmp)
for i in ran(num) :
    tmp = heapq.heappop(heap)
    print(tmp)