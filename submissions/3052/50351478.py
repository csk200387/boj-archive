dic = {}
for i in range(0,10):
    num = int(input("")) % 42
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(len(dic.keys()))