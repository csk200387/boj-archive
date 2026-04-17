div = int(input())
num = sorted(list(map(int,input().split())),reverse=True)
maxs = num[0]
for i in range(0,len(num)):
    num[i] = (num[i]/maxs)*100
print(sum(num)/div)