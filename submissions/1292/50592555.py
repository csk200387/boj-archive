ar = []
for i in range(1,1000) :
    for l in range(1,i+1) :
        ar.append(i)
    if len(ar) >= 1000 :
        break
n = list(map(int,input().split()))
print(sum(ar[n[0]-1:n[1]]))