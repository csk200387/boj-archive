import heapq as h
n, *arr = map(int, open(0))
r = 0
for i in range(0,n-1):
  a = h.heappop(arr)
  b = h.heappop(arr)
  res += a+bs
  h.heappush(arr,a+b)
print(r)