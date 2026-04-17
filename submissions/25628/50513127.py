n = list(map(int,input().split()))
bre, pat = n[0], n[1]
print(bre//2 if bre//2 < pat else pat)