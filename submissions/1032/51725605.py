import sys
input = lambda:sys.stdin.readline().rstrip()
ar = []
n = int(input())
first = input()
res = ""
for i in range(n-1) :
    tmp = input()
    for l in range(len(first)) :
        if first[l] != tmp[l] :
            res += "?"
        else :
            res += first[l]
    first = res
    res = ""
print(first)