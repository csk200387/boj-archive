import sys
input = lambda:int(sys.stdin.readline())

n = input()
c = input()
arr = [input() for _ in range(c)]
arr.sort()


s, cnt, i = 0, 0, 0
while s <= n:
    s += arr[i]
    if s > n:
        s -= arr[i]
        break
    i += 1
print(i)