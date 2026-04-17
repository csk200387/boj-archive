import sys
input = lambda:sys.stdin.readline().rstrip()
H, W = map(int, input().split())
result = [0, 0, 0, 0, 0]
for h in range(H):
    input()
    layers = [input() for i in range(4)]
    for w in range(W):
        tmp = 0
        for l in range(4):
            if layers[l][1+5*w] == '*':
                tmp += 1
        result[tmp] += 1
input()
print(*result)