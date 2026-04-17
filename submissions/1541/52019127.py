a = input()
a = a.split("-")
res = []
for i in a :
    tmp = []
    for l in i.split("+") :
        tmp.append(l.lstrip("0"))
    i = "+".join(tmp)
    #print(i)
    res.append(str(eval(str(i))))
print(eval("-".join(res)))