n=int(input())
a=[[*map(int,input().split())]for _ in range(n)]
a.sort(key=lambda x:(x[0],x[1]))
for i in a:print(*i)