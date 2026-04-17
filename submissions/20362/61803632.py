import sys
input = lambda:sys.stdin.readline().rstrip()

N, S = input().split()

chats = []
answer = ''
for idx in range(int(N)):
    n, c = input().split()
    if n == S:
        answer = c
    chats.append([n,c])
ct = 0
idx = 0
while True:
    if chats[idx][0] == S:
        break
    else:
        if chats[idx][1] == answer:
            ct += 1
    idx += 1
print(ct)