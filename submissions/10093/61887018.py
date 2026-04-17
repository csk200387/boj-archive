a,b=map(int,input().split())
arr=[i for i in range(min(a,b)+1,max(a,b))]
print(len(arr))
print(*arr)