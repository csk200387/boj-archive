import heapq as h
ar = []
for _ in range(int(input())) :
    t = int(input())
    if t == 0 :
        print(0 if len(ar) == 0 else -h.heappop(ar))
    else :
        h.heappush(ar, -t)