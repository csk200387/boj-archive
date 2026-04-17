N, K = map(int,input().split())
arr = []
tmp = [i for i in range(1,N+1)] 
num = 0
for _ in range(N):
    num += K-1
    if num >= len(tmp) :
        num %= len(tmp)
    arr.append(str(tmp[num]))
    tmp.pop(num)
print("<", end="")
print(*arr, sep=", ", end="")
print(">")