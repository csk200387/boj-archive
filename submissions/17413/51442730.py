import re
p = re.compile("<[^>]*>?")
inp = input()
splited_arr = re.split(p,inp)
print(splited_arr)
for i in splited_arr :
    if i != "" :
        tmp = []
        for l in i.split(" ") :
            tmp.append(l[::-1])
        a = " ".join(tmp)
        inp = inp.replace(i, a)
print(inp)