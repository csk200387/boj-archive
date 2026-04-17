n = int(input())
a, b = 0, 1
for i in range((n-1)%1500000):
    a, b = b, (a+b)%1_000_000
print(b)