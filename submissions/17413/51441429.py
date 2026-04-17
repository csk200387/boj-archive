import re
p = re.compile('(<([^>]+)>)')
res = []
inp = input()
i = 0
if p.search(inp) == None:
    arr = inp.split()
    for i in arr :
        res.append(i[::-1])
    print(" ".join(res))
else :
    arr = re.split(p,inp)
    while i < len(arr) :
        if p.match(arr[i]) :
            res.append(arr[i])
            i += 1
        else :
            res.append(arr[i][::-1])
        i += 1
    print("".join(res))