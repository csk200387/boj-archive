a,b,c=map(int,input().split())
d=[i+j+k for i in range(1,a+1) for j in range(1,b+1) for k in range(1,c+1)]
print(max(d, key=d.count))