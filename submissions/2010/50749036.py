import sys
input = sys.stdin.readline
num = int(input().rstrip())
res = 0
for i in range(num) :
    a = int(input().rstrip())
    res += a-1
print(res+1)