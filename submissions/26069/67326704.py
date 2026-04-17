from sys import stdin
input = lambda:stdin.readline().rstrip()
n = int(input())
dance = {"ChongChong"}
for _ in range(n):
    a,b = input().split()
    if b in dance:
        if a not in dance:
            dance.add(a)
    elif a in dance:
        if b not in dance:
            dance.add(b)
print(len(dance))