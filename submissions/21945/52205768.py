a = input()
ar = input().split()
res = 0
for i in ar :
    if i == i[::-1] :
        res += int(i)
print(res)