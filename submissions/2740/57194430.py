import sys
input = lambda:sys.stdin.readline().rstrip()
_is = lambda:input().split()
lm = lambda:list(map(int, _is()))
n1 = int(_is()[0])
a1 = [lm() for _ in range(n1)]
n2 = int(_is()[0])
a2 = [lm() for _ in range(n2)]
for i in range(n1) :
    a = [sum(a1[i][l]*a2[l][h] for l in range(len(arr2))) for h in range(len(arr2[0]))]
    print(*a)