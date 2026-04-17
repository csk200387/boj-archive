n, k = map(int, input().split())
last = 0
len = 1
ct = 9
while k > len*ct:
    k -= len*ct
    last += ct
    len += 1
    ct = ct*10
last = (last+1) + ((k-1) // len)
if last > n:print(-1)
else:print(str(last)[ (k-1) % len])