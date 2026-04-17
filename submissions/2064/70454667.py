import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
arr = ["".join(map(lambda x: bin(int(x))[2:].zfill(8), input().split("."))) for _ in range(N)]

m = 0
for ip in arr:
    for i in range(32):
        if arr[0][i] != ip[i]:
            m = max(m, 32-i)

network = arr[0][:-m] + '0'*m
mask = '1'*(32-m) + '0'*m
if m == 0:
    network = arr[0]
print(".".join([str(int(network[i:i+8], 2)) for i in range(0, 32, 8)]))
print(".".join([str(int(mask[i:i+8], 2)) for i in range(0, 32, 8)]))