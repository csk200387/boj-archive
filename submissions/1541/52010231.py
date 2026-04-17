a = input()
a = a.split("-")
res = []
for i in a :
    print(i)
    res.append(str(eval(str(int(i)))))
print(eval("-".join(res)))