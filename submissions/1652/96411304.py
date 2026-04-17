import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []
w, l = 0, 0
for i in range(n):
    arr.append(input())
    if arr[-1].find("..") != -1:
        w += 1

for i in range(n):
    txt = ""
    for t in range(n):
        txt += arr[t][i]
    if txt.find("..") != -1:
        l += 1
print(w, l)