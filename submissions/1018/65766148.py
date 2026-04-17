import sys
input = lambda:sys.stdin.readline().rstrip()
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
r = []
for i in range(N-7):
    for l in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for j in range(i, i+8):
            for k in range(l, l+8):
                if (j+k)%2 == 0:
                    if arr[j][k] != 'W':
                        cnt1 += 1
                    if arr[j][k] != 'B':
                        cnt2 += 1
                else:
                    if arr[j][k] != 'B':
                        cnt1 += 1
                    if arr[j][k] != 'W':
                        cnt2 += 1
        r.append(cnt1)
        r.append(cnt2)
print(min(r))