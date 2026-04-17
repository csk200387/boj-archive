import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
ar = []
for i in range(n) :
    a = input().rstrip().split()
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
        ar = sorted(ar)
        print(ar[0] if len(ar) != 0 else -1)
    elif cmd == "back" :
        ar = sorted(ar)
        print(ar[-1] if len(ar) != 0 else -1)