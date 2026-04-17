import sys
input = lambda:sys.stdin.readline().rstrip()
dic = {}
for _ in range(int(input())) :
    a, b = input().split()
    dic[a] = b
arr = []
for _ in range(int(input())) :
    arr.append(input())
result = ""
for c in arr:
    if c in dic:
        result += dic[c]
    else:
        result += c
print(result)