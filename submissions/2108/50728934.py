from collections import Counter
num = int(input())
ar = []
for i in range(num) :
    ar.append(int(input()))

cnt = Counter(ar)
print(round(sum(ar)/num))
print(sorted(ar)[round(num/2)])

print(list(cnt.keys())[0])
print(max(ar)-min(ar))