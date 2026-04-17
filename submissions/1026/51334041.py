res = 0
n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())), reverse=True)
for i in range(n) :
    res += a[i]*b[i]
print(res)