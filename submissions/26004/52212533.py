d = {}
n = int(input())
inp = input()
for i in inp :
    if i in ["H", "I", "A", "R", "C"] :
        try :
            d[i] += 1
        except :
            d[i] = 1
if len(d.keys()) != 5 :
    print(0)
else :
    print(min(d.values()))