import sys
dic = {}
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n in dic:dic[n] += 1
    else:dic[n] = 1
print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])