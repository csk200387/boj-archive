n,m,k = map(int, input().split())
M,K,c=0,-n,0
while M>K:
 M+=m
 K+=k
 c+=1
print(c)