a = int(input(""))
res = []
for i in range(0,a):
    res.append(int(input()))
print("\n".join(map(str,sorted(res))))