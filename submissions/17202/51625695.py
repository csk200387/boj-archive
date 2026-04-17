A = list(input())
B = list(input())
arr = list(map(int,A+B))
tmp = []
while len(arr) > 2 :
    #print(arr)
    t = []
    for i in range(1,len(arr)) :
        t.append((int(arr[i-1]+int(arr[i]))%10))
    arr = t
#print(arr)
print(*arr, sep="")