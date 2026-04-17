import sys
input = lambda:sys.stdin.readline().rstrip()
n, a = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start = sum(arr)//a
while True:
    cnt = 0
    for i in arr:
        cnt += i//start
    if cnt == a:
        break
    start -= 1
print(start)