import heapq
ar = []
for _ in range(int(input())) :
    heapq.heappush(ar,int(input()))
ar.sort()
tmp = []
for i in ar :
    stack = 0
    for l in range(i,i+5) :
        if l in ar :
            stack += 1
    tmp.append(stack)
print(5-max(tmp))