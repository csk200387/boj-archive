a,b,c = 1,1,1
n = int(input())
for _ in range(n-3):
    a,b,c = b,c,a+c
print(c)