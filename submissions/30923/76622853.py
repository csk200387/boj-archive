n=int(input())
arr=list(map(int,input().split()))
print(sum([abs(arr[i]-arr[i-1])for i in range(1,n)])+n*2+arr[0]+arr[-1]+sum(arr)*2)