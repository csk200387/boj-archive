res = 0
tmp = 1
for i in range(int(input())) :
    res += tmp
    tmp = res - tmp
print(res)