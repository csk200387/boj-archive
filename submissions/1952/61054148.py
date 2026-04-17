n, m = map(int, input().split())
print((min(n,m)-1)*2+1 if n != m else (n-1)*2)