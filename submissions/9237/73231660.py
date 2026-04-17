input()
print(sum(max(enumerate(sorted(map(int,input().split()),reverse=1),1),key=sum))+1)