a, b = map(int, input().split())
res = 1
for i in range(2, a+1):
    res = (res*i)%b
print(res%b)