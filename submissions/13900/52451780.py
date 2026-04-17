input()
a = list(map(int, input().split()))
t = sum(a)
res = 0
for i in a :
    t -= i
    res += t*i
print(res)