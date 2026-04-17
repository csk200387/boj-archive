import re
res = []
for i in range(5) :
    t = input()
    if "FBI" in t :
        res.append(i+1)
res = " ".join(map(str,res))
print(res if len(res) != 0 else "HE GOT AWAY!")