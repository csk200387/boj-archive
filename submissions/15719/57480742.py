n = int(input())
r = sum(map(int, input().split()))
sum = n*(n+1)//2
print(n-sum+r)