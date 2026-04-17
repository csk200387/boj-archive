import sys, re
input = lambda:sys.stdin.readline().rstrip()
res = []
for i in range(5) :
    t = input()
    if re.fullmatch(r"^(?=.*[A-Z])(?=.*\-)(?=.*\d)[A-Z\-\d]+$", t) != None and "FBI" in t:
        res.append(i+1)
res = " ".join(map(str,res))
print(res if len(res) > 0 else "HE GOT AWAY!")