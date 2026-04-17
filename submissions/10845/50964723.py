import heapq

n = int(input())
ar = []
for i in range(n) :
    a = input().split()
    cmd = a[0]
    if cmd == "push" :
        val = int(a[1])
        heapq.heappush(ar,val)
    elif cmd == "pop" :
        try :
            print(heapq.heappop(ar))
        except :
            print(-1)
    elif cmd == "size" :
        print(len(ar))
    elif cmd == "empty" :
        print(1 if len(ar) == 0 else 0)
    elif cmd == "front" :
        print(ar[0] if len(ar) != 0 else -1)
    elif cmd == "back" :
        print(ar[-1] if len(ar) != 0 else -1)