n, m = map(int, input().split())
print((n+m)*(max(n, m)-min(n, m)+1)//2)