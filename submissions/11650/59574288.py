num = int(input())
ar = [[*map(int,input().split())] for _ in range(num)]
ar.sort(key=lambda x:(x[0], x[1]))
for i in ar :
    print(*i)