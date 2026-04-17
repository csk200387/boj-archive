import sys
input = lambda:sys.stdin.readline().rstrip()
_is = lambda:input().split()
lm = lambda:list(map(int, _is()))
n1 = int(_is()[0])
arr1 = [lm() for _ in range(n1)]
n2 = int(_is()[0])
arr2 = [lm() for _ in range(n2)]
for i in range(n1) :
    a = []
    for h in range(len(arr2[0])) :
        tmp = 0
        for l in range(len(arr2)) :
            tmp += arr1[i][l]*arr2[l][h]
        a.append(tmp)
    print(*a)