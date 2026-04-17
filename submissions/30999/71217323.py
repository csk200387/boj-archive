import sys
input = lambda:sys.stdin.readline().rstrip()
a, b = map(int, input().split())
cnt = 0
for i in range(a):
    data = input()
    if data.count("O") > len(data)//2:
        cnt += 1
print(cnt)