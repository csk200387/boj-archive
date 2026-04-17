import heapq
ar = []
stack = 1
for _ in range(int(input())) :
    heapq.heappush(ar,int(input()))
tmp = [1]
ar.sort()
for i in range(1,len(ar)) :
    if ar[i] == ar[i-1]+1 :
        stack += 1
        tmp.append(stack)
    else :
        stack = 1
print(5-max(tmp))