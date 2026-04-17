al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ki = "DEFGHIJKLMNOPQRSTUVWXYZABC"
a = input()
res = []
for i in a :
    res.append(al[ki.index(i)])
print("".join(res))