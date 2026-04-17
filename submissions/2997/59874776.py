a,b,c=sorted(map(int,input().split()))
print(c-b+a if b-a<c-b else c-a+b)