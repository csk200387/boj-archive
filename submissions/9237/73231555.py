n=int(input())
arr=sorted(map(int,input().split()),reverse=1)
print(sum(max(enumerate(arr,1),key=sum))+1)