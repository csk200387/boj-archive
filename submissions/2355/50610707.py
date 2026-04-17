res = 0
num = list(map(int,input().split()))
for i in range(num[0],num[1]+1) :
    res += i
print(res)