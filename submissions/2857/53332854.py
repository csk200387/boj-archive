import sys
arr = sys.stdin.readlines()
res = []
for i in range(5) :
    if "FBI" in arr[i] and "-" in arr[i] :
        res.append(i+1)
a = " ".join(map(str,res))
print(a if len(res)>0 else "HE GOT AWAY!")