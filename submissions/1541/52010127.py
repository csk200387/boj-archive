a = input()
a = a.split("-")
res = []
for i in a :
    res.append(str(eval(i)))
print(eval("-".join(res)))