num = list(map(int,input().split()))
arr = list(range(1,num[0]+1))
res = []
for i in range(num[0]) :
    for l in range(num[1]) :
        if l == num[1]-1 :
            res.append(arr.pop(0))
        else :
            arr.append(arr.pop(0))
a = ", ".join(list(map(str,res)))
print(f"<{a}>")