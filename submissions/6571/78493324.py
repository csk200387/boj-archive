import sys
input = lambda:sys.stdin.readline().rstrip()

dp = [0, 1]
while True:
    tmp = dp[-1] + dp[-2]
    dp.append(tmp)
    if tmp >= 10**100:
        break

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    cnt = 0
    for i in dp:
        if a <= i <= b:
            cnt += 1
    print(cnt)