a,b = map(int, input().split())
arr = list(range(1,a+1))
res = []
for i in range(a) :
    for l in range(b) :
        if l == b-1 :
            res.append(arr.pop(0))
        else :
            arr.append(arr.pop(0))
a = ", ".join(list(map(str,res)))
print(f"<{a}>")