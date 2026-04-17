import sys
input = lambda:sys.stdin.readline().rstrip()
dic = {}
n = int(input())
for _ in range(n):
    exe = input().split(".")[-1]
    if exe in dic:
        dic[exe] += 1
    else:
        dic[exe] = 1

for k in sorted(dic):
    print(k, dic[k])